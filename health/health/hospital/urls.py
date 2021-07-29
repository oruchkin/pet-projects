from django.urls import path
from . import views

urlpatterns = [    
    path('hospitalsdata/', views.getHospitals, name="allhospitals"),
]



