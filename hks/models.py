from django.db import models

# Create your models here.
from unicodedata import category
from django.db import models
from django.contrib.auth.models import AbstractUser,User
# Create your models here.
class User1(AbstractUser):
    is_Doctor = models.BooleanField('Docotr status', default=False)
    is_Patient = models.BooleanField('Patient status', default=False)

class profile_details(models.Model):
    user = models.ForeignKey(User1,related_name='profile_details',on_delete=models.CASCADE)
    imgp=models.FileField(upload_to='imgs',null=True,blank=True)
    u_nm=models.CharField(max_length=150)
    fstname=models.CharField(max_length=250)
    secname=models.CharField(max_length=250)
    terimail=models.EmailField()
    timestamp = models.DateTimeField(null=True)
    address1 = models.CharField(
        "Address line 1",
        max_length=1024,
    )
    pincode=models.IntegerField(default=None)
    city = models.CharField(
        "City",
        max_length=1024,
    )
    state = models.CharField(
        "state",
        max_length=1024,
    )

class Meeting(models.Model):
    doc=models.ForeignKey(User1,related_name='doctor',on_delete=models.CASCADE)
    pat=models.ForeignKey(User1,related_name='patient',on_delete=models.CASCADE)
    date=models.DateField(null=True)
    time=models.TimeField(null=True)
    duration=models.IntegerField(default=0)

       