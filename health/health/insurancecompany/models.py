from django.db import models

# Create your models here.

class Company(models.Model):
    insurance_company_id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length = 100)
    details = models.TextField()
    
    
    def __str__(self):
        return self.company_name

