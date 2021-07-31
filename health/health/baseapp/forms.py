
from django import forms
from django.db.models import fields
from .models import Contact

#this is WITHOUT database
class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    mobile = forms.IntegerField()
    
    
#this is WITH database
class ContactModelForm(forms.ModelForm):

    name = forms.CharField(label="name", help_text="enter your name(help_text)", widget=forms.TextInput(attrs={
        "class":"form-control"
    }))
    email = forms.EmailField(label="email", widget=forms.EmailInput(attrs={
        "class": "form-control"
    }))
    mobile = forms.CharField(label="phone", max_length=9, widget=forms.TextInput(attrs={
        "class": "form-control"
    }))
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={
        "class": "form-control"
    }))
    

    #this is important
    #this is how to obtain fields from "contact" model, for not copying them twice
    class Meta:
        model=Contact
        fields='__all__' #all fields from "Contact model"
        #fields=['name','email'] #this is how to choose only few fields

    
    
    

