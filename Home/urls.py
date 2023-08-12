from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns =  [
    path('', views.index, name='mainpage'),
    path('interest',login_required(views.interest), name='interest'),
    path('register/',views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/',auth_views.LogoutView.as_view(next_page='/Home'),name='logout'),
    path('lowest_below_1_month/', login_required(views.lowest1), name='lowest1'),
    path('lowest_1_month/', login_required(views.lowest2), name='lowest2'),
    path('lowest_2_month/', login_required(views.lowest3), name='lowest3'),
    path('lowest_3_month/', login_required(views.lowest4), name='lowest4'),
    path('lowest_4_month/', login_required(views.lowest5), name='lowest5'),
    path('lowest_5_month/', login_required(views.lowest6), name='lowest6'),
    path('lowest_6_month/', login_required(views.lowest7), name='lowest7'),
    path('lowest_7_month/', login_required(views.lowest8), name='lowest8'),
    path('lowest_8_month/', login_required(views.lowest9), name='lowest9'),
    path('lowest_9_month/', login_required(views.lowest10), name='lowest10'),
    path('lowest_10_month/', login_required(views.lowest11), name='lowest11'),
    path('owest_11_month/', login_required(views.lowest12), name='lowest12'),
    path('lowest_12_month/', login_required(views.lowest13), name='lowest13'),
    path('lowest_24_month/', login_required(views.lowest14), name='lowest14'),
    path('lowest_36_month/', login_required(views.lowest15), name='lowest15'),
]