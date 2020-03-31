from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('index.html', views.homepage, name='homepage2'),
    path('utilities.html', views.utilities, name='utilities'),
    path('view_past_orders.html', views.view_past_orders, name='view_past_orders'),
    path('buyer_prediction_tool.html', views.buyer_prediction_tool, name='buyer_prediction_tool')
]