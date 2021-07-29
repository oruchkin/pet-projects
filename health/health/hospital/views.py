from django.shortcuts import render

from . models import Hospital

# Create your views here.


def getHospitals(request):
    # model query get the data from the model
    all_hospitals = Hospital.objects.all() # SELECT * from hospital_hospital
    return render(request, "baseapp/hospitals.html", {
        "all_hospitals_key": all_hospitals,
    })
