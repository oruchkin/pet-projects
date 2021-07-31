from django.shortcuts import render
from django.http import HttpResponse
from hospital.models import Hospital
from patient.models import Patient
from django.db.models import Q
from django.db.models import Avg, Max

from .forms import ContactForm, ContactModelForm

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

    patient_avg_age = Patient.objects.all().aggregate(Avg('age'),Max('age'))

    patient_count = Patient.objects.all().count

    context = {

        "patients_age_greaterthan35_key": patients_age_greaterthan35,
        "original_query1": "Patient.objects.filter(age__gt=10)",
        
        "patient_fname_lastname_key": patient_fname_lastname,
        "original_query2": "Patient.objects.filter(first_name__startswith='J') | Patient.objects.filter(last_name__startswith='c')",
        
        "patient_firtstname_exclude_j": patient_firtstname_exclude_j,
        "original_query3": "Patient.objects.exclude(first_name__istartswith='j')",
        
        "patients_nth_record": patients_nth_record,
        "original_query4": "Patient.objects.order_by('dateofbirth')[1]",

        "patient_avg_age": patient_avg_age,
        "original_query5": "Patient.objects.all().aggregate(Avg('age'),Max('age'))",

        "patient_count": patient_count,
        "original_query6": "Patient.objects.all().count",

    }
    #functions
    #all() #filter() # exclude() # get() #aggregate() #order_by() #count()
    return render(request,"baseapp/modelQueries.html",context)


def contactView(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse('Your data is submited')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, "baseapp/contact.html", {
        "form": form,
    })


def ContactModelFormView(request):
    if request.method=="POST":
        form = ContactModelForm(request.POST)
        if form.is_valid():
            #save the data into database table.
            form.save()
            return HttpResponse('Your data is submited')

    else:
        form = ContactModelForm()

        return render(request, 'baseapp/contactus.html',{
            'form_key': form
        })

