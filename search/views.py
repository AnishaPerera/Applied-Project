from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import vulnerability_detail
from logs.models import SearchLog, AdvancedSearchLog
from .forms import SearchForm, AdvancedSearchForm, UpdateSearchForm
from django.http import HttpResponse
from django.urls import reverse
import requests

# Create your views here.

@login_required
def search(request):

    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            brand = form.cleaned_data.get('brand')
            firmware_version = form.cleaned_data.get('firmware_version')
            
            SearchLog.objects.create(user=request.user, brand=brand, firmware_version=firmware_version)

            query = vulnerability_detail.objects.filter(Q(description__icontains=brand) & Q(description__icontains=firmware_version)).order_by('cve_id')

        
            if not query:
                messages.success(request, 'No results found')

            return render(request, 'search/search_results.html', {'search_results': query})

    else:
        form  = SearchForm()
        return render(request, 'search/search.html', {'form': form})
    

@login_required
def advanced_search(request):
    if request.method == 'POST':
        form = AdvancedSearchForm(request.POST)

        if form.is_valid():
            brand = form.cleaned_data.get('brand')
            firmware_version = form.cleaned_data.get('firmware_version')
            cveid = form.cleaned_data.get('cveid')
            userquery = form.cleaned_data.get('userquery')
            api_slider = form.cleaned_data.get('api_slider')
            api_slider2 = form.cleaned_data.get('api_slider2')


            AdvancedSearchLog.objects.create(user=request.user, brand=brand, firmware_version=firmware_version, cve_id=cveid,userquery=userquery)
            
            if api_slider or api_slider2:
                url = 'https://services.nvd.nist.gov/rest/json/cves/2.0'

                if cveid:
                    apireq = url+'?cveId='+cveid
    
                    if apireq:
                            connection,query_result = get_info(apireq)
                            
                            if connection == True:
                                return render(request, 'search/advanced_details.html', {'vuln_instance': query_result})
                            else:
                                messages.success(request, 'No results found')
                                return render(request, 'search/search_results.html', {'search_results': query_result})
                elif userquery:
                    apireq = url+'?keywordSearch='+userquery
        
                    if apireq:
                        response = requests.get(apireq)

                        if response.status_code == 200:
                            results = response.json()
                            cvelist=[]

                            for r in results['vulnerabilities']:
                                cve_id = r["cve"]["id"]

                                cvelist.append(cve_id)

                           
                            return render(request, 'search/advanced_search_results.html', {'search_results': cvelist})

                        else:
                            cvelist = []
                            messages.success(request, 'No results found')

                            return render(request, 'search/search_results.html', {'search_results': query_result})
                        
            else:
                filters = Q()

                if brand:
                    filters &= (Q(description__icontains = brand))        
                if firmware_version:    
                    filters &= (Q(description__icontains = firmware_version))
                if cveid:
                    filters &= (Q(cve_id = cveid))
                if userquery:
                    filters &= (Q(description__icontains = userquery))
                
                if filters:
                    query_result = vulnerability_detail.objects.filter(filters)
                    
                    if not query_result:
                        messages.success(request, 'No results found')
                else:
                    query_result=[]
                    messages.success(request, 'No results found')

                return render(request, 'search/search_results.html', {'search_results': query_result})
    else:
        form = AdvancedSearchForm()
        return render(request, 'search/advanced_search.html', {'form': form})
    

def get_info(apireq):
    response = requests.get(apireq)

    if response.status_code == 200:
        results = response.json()

        for r in results['vulnerabilities']:
            cve_id = r["cve"]["id"]
            cve_published = r["cve"]["published"]
            cve_description = r["cve"]["descriptions"][0]["value"]
            cvss_baseSeverity = r["cve"]["metrics"]["cvssMetricV2"][0]["baseSeverity"]
            try:
                cvss_metricv31 = r['cve']['metrics']['cvssMetricV31'][0]['cvssData']
            except KeyError:
                pass
            else:                        
                base_score = cvss_metricv31['baseScore']

                query_result = [vulnerability_detail(cve_id=cve_id, published_date=cve_published,
                description=cve_description, base_severity=cvss_baseSeverity, cvss_score=base_score)]

                break

            try:
                cvss_metricv3 = r['cve']['metrics']['cvssMetricV3'][0]['cvssData']
            except KeyError:
                pass
            else:                        
                base_score = cvss_metricv3['baseScore']

                query_result = [vulnerability_detail(cve_id=cve_id, published_date=cve_published,
                description=cve_description, base_severity=cvss_baseSeverity, cvss_score=base_score)]

                break

            try:
                cvss_metricv2 = r['cve']['metrics']['cvssMetricV2'][0]['cvssData']
            except KeyError:
                pass
            else:                        
                base_score = cvss_metricv2['baseScore']

                query_result = [vulnerability_detail(cve_id=cve_id, published_date=cve_published,
                description=cve_description, base_severity=cvss_baseSeverity, cvss_score=base_score)]

                break

        return(True, query_result)        
    else:
        query_result = []
        return(False, query_result)

@login_required
def advancedsearch_details(request, cve_id):
    apireq = 'https://services.nvd.nist.gov/rest/json/cves/2.0?cveId='+cve_id    
    connection,query_result = get_info(apireq)
    
    if connection == True: 
        return render(request, 'search/advanced_details.html', {'vuln_instance': query_result})
    else:
        messages.success(request, 'Error cant find CVE Details')
        return render(request, 'search/search_results.html', {'search_results': query_result})
    

@login_required
def details(request, cve_id):
    vuln_instance = get_object_or_404(vulnerability_detail, cve_id=cve_id)
    return render(request, 'search/details.html', {'vuln_instance': vuln_instance})

def updates(request):
    if request.method == 'POST':
        form  = UpdateSearchForm(request.POST)
        if form.is_valid():
            date1 = form.cleaned_data.get('date1')
            date2 = form.cleaned_data.get('date2')

            connection,details = get_update_info(date1,date2)

            if connection == True:
                return render(request, 'search/update_results.html', {'results': details})
            
            else:
                messages.success(request, 'Failed Try Again')


            return redirect('updatepage')

    else:
        form = UpdateSearchForm()
    return render(request, 'search/updates.html', {'form':form})


def get_update_info(date1,date2):
    if str(date1) == str(date2):
        apireq = 'https://services.nvd.nist.gov/rest/json/cves/2.0/?pubStartDate='+str(date1)+'T00:00:00.000&pubEndDate='+str(date2)+'T23:59:59.999'
    else:
        apireq = 'https://services.nvd.nist.gov/rest/json/cves/2.0/?pubStartDate='+str(date1)+'T00:00:00.000&pubEndDate='+str(date2)+'T00:00:00.000'

    response = requests.get(apireq)

    if response.status_code == 200:
        results = response.json()
        details=[]

        for r in results['vulnerabilities']:
            cve_id = r["cve"]["id"]
            cve_published = r["cve"]["published"]
            cve_description = r["cve"]["descriptions"][0]["value"]

            details.append({'cve_id':cve_id, 'cve_published':cve_published, 'cve_description': cve_description})        
        
        return(True, details)

    else:
        return(False,{})



@login_required
def get_pdf(request,cve_id):
    try:
        obj = vulnerability_detail.objects.get(cve_id=cve_id)
    except vulnerability_detail.DoesNotExist:
        messages.error(request, 'Unable to Download PDF')
        return redirect(reverse('searchpage'))
    
    else:
        content = {'obj':obj}
        
        template = get_template('search/pdf.html')
        html = template.render(content)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{obj.pk}.pdf"'

        pisa_status = pisa.CreatePDF(html, dest=response,encoding='utf-8')

        if pisa_status.err:
            return HttpResponse('Error <pre>'+html+'</pre>')
        return response