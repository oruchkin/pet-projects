from django.shortcuts import render
from django.http import HttpResponse
from hospital.models import Hospital
from patient.models import Patient
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request,"baseapp/index.html")

def all_model_quiries(request):
    patients_age_greaterthan35 = Patient.objects.filter(age__gt=10)
    #age__lt(larger than), age_eq(equal), age__ne (not equal) age__gt(greater than)

    # patient_fname_lastname = Patient.objects.filter(
    #     first_name__startswith='J') | Patient.objects.filter(last_name__startswith='c')

    patient_fname_lastname = Patient.objects.filter(Q(first_name__startswith='J') | Q(last_name__startswith='c'))
   
    patient_firtstname_exclude_j = Patient.objects.exclude(first_name__istartswith='j')

    patients_nth_record = Patient.objects.order_by("dateofbirth")[1]


    context = {

        "patients_age_greaterthan35_key": patients_age_greaterthan35,
        "original_query1": "Patient.objects.filter(age__gt=10)",
        
        "patient_fname_lastname_key": patient_fname_lastname,
        "original_query2": "Patient.objects.filter(first_name__startswith='J') | Patient.objects.filter(last_name__startswith='c')",
        
        "patient_firtstname_exclude_j": patient_firtstname_exclude_j,
        "original_query3": "Patient.objects.exclude(first_name__istartswith='j')",
        
        "patients_nth_record": patients_nth_record,
        "original_query4": "Patient.objects.order_by('dateofbirth')[1]"
    }

    return render(request,"baseapp/modelQueries.html",context)

