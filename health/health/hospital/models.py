from django.db import models
from datetime import datetime

# Create your models here.

class Hospital_Type(models.Model):
    type_name = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 50)
    
    def __str__(self):
        return self.type_name
    


class Hospital(models.Model):
    hospital_id = models.IntegerField(primary_key=True)
    category = models.ForeignKey(Hospital_Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length = 50)
    address = models.TextField()
    updated_date = models.DateTimeField(default=datetime.now)
    # for image blank=True, null=True means it is not required
    logo = models.ImageField(upload_to="images/hospital/", blank=True, null=True)
    
    def __str__(self):
        return self.name

