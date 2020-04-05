from django.shortcuts import render
from .models import Utilities
import datetime

# libraries needed for the webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

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

def groceries(request):
    if request.method == 'POST':
        chrome_options = Options()
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("https://primenow.amazon.com/home")
        
    return render(request, 'pages/groceries.html', {})
 
def input_corrected_orders(request):
    return render(request, 'pages/input_corrected_orders.html', {})