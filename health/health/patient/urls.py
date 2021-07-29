from django.urls import path
from . import views

urlpatterns = [

    path('allpatients/', views.getAllPatients, name="patients"),
]
