from django.contrib import admin
from . models import Hospital_Type, Hospital

# Register your models here.

# django custom admin screens
admin.site.site_header = "HIC Admin"
admin.site.site_title = "HIC Admin Portal"
admin.site.index_title = "Welcome to Hospital Insurance Claims"


class HospitalAdmin(admin.ModelAdmin):
    #this is slug key that takes name ask a value in tupple
    #it fill in slug with converted name
    prepopulated_fields={
        "slug":('name',)
    }


admin.site.register(Hospital_Type)
admin.site.register(Hospital, HospitalAdmin)
