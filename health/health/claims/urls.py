from django.urls import path
from . import views

urlpatterns = [

    path('claimdata/', views.getClaimsData, name="AllClaimsData"),
    
]
