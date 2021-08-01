from django.urls import path
from . import views

urlpatterns = [
    
    path('registration/', views.signup_view, name="signup_view"),
    path('login/', views.loginView, name="login"),
    path('logout/', views.logout_view, name="logout"),
]

