from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns =  [
    path('', views.index),
    path('interest/',login_required(views.interest), name='interest'),
    path('register/',views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/',auth_views.LogoutView.as_view(next_page='/Home/'),name='logout'),
    path('lowest_below_1_month/', login_required(views.lowest1), name='below 1 month'),
    path('lowest_1_month/', login_required(views.lowest2), name='1 month'),
    path('lowest_2_month/', login_required(views.lowest3), name='2 months'),
    path('lowest_3_month/', login_required(views.lowest4), name='3 months'),
    path('lowest_4_month/', login_required(views.lowest5), name='4 months'),
    path('lowest_5_month/', login_required(views.lowest6), name='5 months'),
    path('lowest_6_month/', login_required(views.lowest7), name='6 months'),
    path('lowest_7_month/', login_required(views.lowest8), name='7 months'),
    path('lowest_8_month/', login_required(views.lowest9), name='8 months'),
    path('lowest_9_month/', login_required(views.lowest10), name='9 months'),
    path('lowest_10_month/', login_required(views.lowest11), name='10 months'),
    path('lowest_11_month/', login_required(views.lowest12), name='11 months'),
    path('lowest_12_month/', login_required(views.lowest13), name='12 months'),
    path('lowest_24_month/', login_required(views.lowest14), name='24 months'),
    path('lowest_36_month/', login_required(views.lowest15), name='36 months'),
    path('delete/<int:id>/',login_required(views.delete_history), name='delete_history'),
    path('changeStatus/', login_required(views.changeStatus),name='changeStatus'),
    path('redirectToggle/',login_required(views.redirectToggle), name='redirectToggle'),
]