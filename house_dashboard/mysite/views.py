from django.shortcuts import render
from .models import Utilities
import datetime

# Create your views here.
def homepage(request):
    return render(request, 'pages/index.html', {})

def utilities(request):
    if request.method == 'POST':
        new_utilities = Utilities(utility_type = request.POST.get('utility_field'), date = request.POST.get('date_field'), amount = request.POST.get('amount_field'))
        new_utilities.save() 
        utilities_table = Utilities.objects.all()
        return render(request, 'pages/utilities.html', {"utilities_table": utilities_table})
        
    else: 
        utilities_table = Utilities.objects.all()
        return render(request, 'pages/utilities.html', {"utilities_table": utilities_table})

def view_past_orders(request):
    return render(request, 'pages/view_past_orders.html', {})

def buyer_prediction_tool(request):
    return render(request, 'pages/buyer_prediction_tool.html', {})
 
def input_corrected_orders(request):
    return render(request, 'pages/input_corrected_orders.html', {})