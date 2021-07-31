from django.db import models
from hospital.models import Hospital
from patient.models import Patient
from insurancecompany.models import Company
from datetime import datetime


# Create your models here.

class ClaimStatus(models.Model):
    claim_status_code = models.CharField(max_length = 8)
    status_description = models.TextField()
    
    def __str__(self):
       return self.claim_status_code

class Claim(models.Model):
    claim_number = models.IntegerField(primary_key=True)
    claim_status = models.ForeignKey('ClaimStatus', on_delete=models.CASCADE)
    hospital_id = models.ForeignKey('hospital.Hospital', on_delete=models.CASCADE)
    patient_id = models.ForeignKey('patient.Patient', on_delete=models.CASCADE)
    insurance_company_id = models.ForeignKey('insurancecompany.Company', on_delete=models.CASCADE)
    details = models.TextField()
    update_date = models.DateField()

    def __str__(self):
       return f"{self.claim_number}"
