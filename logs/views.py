from django.shortcuts import render
from .models import SearchLog, AdvancedSearchLog

# Create your views here.

def history(request):
        
    history = SearchLog.objects.filter(user = request.user).order_by('-timestamp')[:5]
    
    adv_history = AdvancedSearchLog.objects.filter(user = request.user).order_by('-timestamp')[:5]

    show_all = request.GET.get('show_all')
    
    if show_all:
        history = SearchLog.objects.filter(user = request.user).order_by('-timestamp')
        adv_history = AdvancedSearchLog.objects.filter(user = request.user).order_by('-timestamp')

    context = {
        'history':history,
        'adv_history':adv_history,
        'show_all':show_all
    }
    

    return render(request, 'logs/history.html', context)