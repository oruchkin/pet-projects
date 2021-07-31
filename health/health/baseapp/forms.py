
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    mobile = forms.IntegerField()
    
    

    
    
    

