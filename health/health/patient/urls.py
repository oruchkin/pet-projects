from django.urls import path
from . import views

urlpatterns = [

    path('allpatients/', views.getAllPatients, name="patients"),
    #path('patient/<int:patientid>/', views.get_patient_info, name="single_patient"),
    #path('patient/<str:slug>/', views.get_patient_info, name="single_patient"),
    path('patient/<slug:name_slug>/', views.get_patient_info, name="single_patient"),
]
