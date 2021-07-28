from django.contrib import admin
from . models import Hospital_Type, Hospital

# Register your models here.


#admin.site.register(Hospital)
admin.site.register(Hospital_Type)



class HospitalAdmin(admin.ModelAdmin):
    #this is slug key that takes name ask a value in tupple
    #it fill in slug with converted name
    prepopulated_fields={
        "slug":('name',)
    }

admin.site.register(Hospital, HospitalAdmin)
