from django.shortcuts import render
from django.http import HttpResponse
from hospital.models import Hospital
from patient.models import Patient

# Create your views here.

def index(request):
    return render(request,"baseapp/index.html")

def all_model_quiries(request):
