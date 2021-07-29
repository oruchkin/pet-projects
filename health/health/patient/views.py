from django.shortcuts import render
from . models import Patient

# Create your views here.

def getAllPatients(request):
    all_patients = Patient.objects.all() # SELECT * FROM patient_patient

    context={
        "all_patients_key": all_patients,
    }
    return render(request, "patient/all_patient.html", context)


def get_patient_info(request, name_slug):
    get_one_patient = Patient.objects.filter(slug=name_slug) 
    #patient is a table, inside it we have all objects, and we need special filter(where)
    #SELECT * FROM patient WHERE patient_id=patientid

    context = {
        "get_one_patient_key": get_one_patient
    }
    return render(request, "patient/patient_details.html", context)
