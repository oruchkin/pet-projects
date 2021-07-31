from django.db import models

# Create your models here.


#this contacts filled via form !!! class ContactModelForm(forms.ModelForm):
class Contact(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    mobile = models.IntegerField()
    message = models.TextField()
    
    
    def __str__(self):
        return self.name

