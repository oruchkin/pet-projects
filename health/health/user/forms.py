from django.contrib.auth.models import User
from django import forms
from django.db.models import fields
from django.forms.widgets import PasswordInput

class SignupForm(forms.ModelForm):

    username = forms.CharField(label='username',widget=forms.TextInput(
        attrs={
            "class":'form-control bg-light'
        }
    ))

    first_name = forms.CharField(label='First name', widget=forms.TextInput(
        attrs={
            "class": 'form-control bg-light',            
        }
    ))

    last_name = forms.CharField(label='Last name', widget=forms.TextInput(
        attrs={
            "class": 'form-control bg-light'
        }
    ))

    email = forms.EmailField(label='E-mail', widget=forms.TextInput(
        attrs={
            "class": 'form-control bg-light'
        }
    ))

    password = forms.CharField(label='password', widget=forms.PasswordInput(
        attrs={
            "class": 'form-control bg-light'
        }
    ))


            


    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
