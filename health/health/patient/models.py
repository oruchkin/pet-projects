from django.db import models

# Create your models here.

GENDER_CHOICES=[
    ('M', 'MALE'),
    ('F','FEMALE'),
    ('O','OTHER'),
]

class Patient(models.Model):
    patient_id = models.IntegerField(primary_key=True)
    first_name = models.CharField("patient's first name",max_length = 30)
    last_name = models.CharField("patient's last name", max_length=30, null=True, blank=True)
    slug = models.SlugField(max_length = 50)
    age = models.PositiveIntegerField()
    gender = models.CharField(choices=GENDER_CHOICES,max_length = 12)
    dateofbirth = models.DateField("patient's birth day")
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=40)
    address = models.TextField()
    profileimage = models.ImageField("Profile image",upload_to="images/patient/", height_field=None, width_field=None, max_length=100)
    
    
    def __str__(self):
        return f"Name {self.first_name} - surname {self.last_name} - birthday: {self.dateofbirth}"

    class Meta:
        verbose_name_plural = "Patients Info"
 
