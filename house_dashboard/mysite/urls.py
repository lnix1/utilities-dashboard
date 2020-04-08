from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('index.html', views.homepage, name='homepage2'),
    path('utilities.html', views.utilities, name='utilities'),
    path('groceries.html', views.groceries, name='groceries')
]