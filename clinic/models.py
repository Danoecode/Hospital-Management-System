from django.db import models
from django.contrib.auth.models import User
#doctor
#patient
#apointment


class Doctor(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="First name")
    second_name = models.CharField(max_length=30, verbose_name="Second name")
    image = models.ImageField(upload_to='photos', blank=True, verbose_name='Photo')
    phone_number=models.CharField(max_length=30, default=None)
    contact_address = models.CharField(max_length=150, default=None)
    employed_date=models.DateField(auto_now=True)
    user=models.OneToOneField(User,default=None, on_delete=models.CASCADE)
   # status = models.BooleanField(default=False)


    def __str__(self):
        return str(self.user.username)


class Patient(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="First name")
    second_name = models.CharField(max_length=30, verbose_name="Second name")
    phone_number = models.CharField(max_length=30, default=None)
    contact_address = models.CharField(max_length=150, default=None)
    #admission_date =  models.DateTimeField(auto_now_add=True, blank=True)
    #discharge_date = models.DateTimeField(auto_now_add=False, blank=True)
    postcode = models.CharField(max_length=3, verbose_name="PostCode")
    user = models.OneToOneField(User,default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='patient', blank=True, verbose_name='patient')
    #status = models.BooleanField(default=False)



    def __str__(self):
        return str(self.user)

class Apointment(models.Model):
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    status=models.BooleanField(default=True)

    def __str__(self):
        return str(self.user)







