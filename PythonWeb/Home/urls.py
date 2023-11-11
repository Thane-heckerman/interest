from django.urls import path    
from .views import Lowest_function, Interest, Index, Register, Delete_history,Change_status,Redirect_toggle
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .views.Delete_history import delete_history
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns =  [
    path('',Index.index ),
    path('interest/',login_required(Interest.interest), name='interest'),
    path('register/',Register.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/',auth_views.LogoutView.as_view(next_page='/Home/'),name='logout'),
    path('lowest/<str:selectedOption>/', login_required(Lowest_function.lowest), name='lowest'),
    path('history/delete/<int:pk>/',login_required(delete_history),name='delete_history'),
    path('changeStatus/<int:user_id>/', login_required(Change_status.changeStatus),name='changeStatus'),
    path('redirectToggle/',login_required(Redirect_toggle.redirectToggle), name='redirectToggle'),
]