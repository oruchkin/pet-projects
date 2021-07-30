from django.contrib import admin
from . models import Patient

# Register your models here.


#admin.site.register(Hospital)

class PatientAdmin(admin.ModelAdmin):
    #this is slug key that takes name ask a value in tupple
    #it fill in slug with converted name
    prepopulated_fields = {
        #"slug": ('last_name','first_name')
        "slug": ['last_name', 'first_name']
    }

    list_display = ['patient_id', 'first_name', 'last_name',
                    'age', 'gender', 'dateofbirth', 'mobile_number', 'address' ]

    

admin.site.register(Patient, PatientAdmin)
