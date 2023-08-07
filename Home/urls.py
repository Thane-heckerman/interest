from django.urls import path
from . import views

urlpatterns =  [
    path('', views.index),
    # path('interest', views.interest, name='interest'),
    path('lowest_below_1_month/', views.lowest1, name='lowest1'),
    path('lowest_1_month/', views.lowest2, name='lowest2'),
    path('lowest_2_month/', views.lowest3, name='lowest3'),
    path('lowest_3_month/', views.lowest4, name='lowest4'),
    path('lowest_4_month/', views.lowest5, name='lowest5'),
    path('lowest_5_month/', views.lowest6, name='lowest6'),
    path('lowest_6_month/', views.lowest7, name='lowest7'),
    path('lowest_7_month/', views.lowest8, name='lowest8'),
    path('lowest_8_month/', views.lowest9, name='lowest9'),
    path('lowest_9_month/', views.lowest10, name='lowest10'),
    path('lowest_10_month/', views.lowest11, name='lowest11'),
    path('owest_11_month/', views.lowest12, name='lowest12'),
    path('lowest_12_month/', views.lowest13, name='lowest13'),
    path('lowest_24_month/', views.lowest14, name='lowest14'),
    path('lowest_36_month/', views.lowest15, name='lowest15'),
]