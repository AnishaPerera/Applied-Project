from django import forms
from datetime import date, timedelta
from .widgets import DatePickerInput

class SearchForm(forms.Form):
    brand = forms.CharField(max_length=100, min_length=2,widget=forms.TextInput(attrs={'placeholder': 'Brand Name'}))
    firmware_version = forms.CharField(label='Firmware Version / Model Number', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Number'}))
    

class AdvancedSearchForm(forms.Form):
    brand = forms.CharField(max_length=100, required=False)
    firmware_version = forms.CharField(max_length=100, required=False, label='Firmware Version / Model Number')
    cveid = forms.CharField(max_length=100, required=False, label='CVE ID')
    userquery = forms.CharField(max_length=100, required=False, label = 'Query')
    api_slider = forms.BooleanField(required=False, label='NVD Search (For CVE ID)')
    api_slider2 = forms.BooleanField(required=False, label='NVD Search (For Query)')
    

class UpdateSearchForm(forms.Form):
    date1 = forms.DateField(label ='Start Date', widget=DatePickerInput(attrs={'max':date.today()-timedelta(days=1)}))
    date2 = forms.DateField(label ='End Date', widget=DatePickerInput(attrs={'max':date.today()}))
    