from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=45,null=False)
    email=models.EmailField(max_length=45,null=False)
    phone=models.CharField(max_length=10,null=False)
    question=models.TextField()
    date=models.DateField(default=timezone.now)




#FEED-BACK MODEL

class  Feedback_Rating(models.Model):
    name=models.CharField(max_length=45,null=False)
    email=models.EmailField(max_length=45,null=False)
    feedback_text=models.TextField() 
    ratings=models.CharField(max_length=4,null=False) 
    date=models.DateField(default=timezone.now)

class Health_Campaign(models.Model):
    Campaign_Name=models.CharField(max_length=100)
    Organizer_Name=models.CharField(max_length=45)
    venue= models.CharField(max_length=50)
    Description=models.TextField()
    Date=models.DateField(default=timezone.now)

class Doctor(models.Model):
    Doctorid=models.CharField(primary_key=True,max_length=20)
    password=models.CharField(max_length=45)
    name=models.CharField(max_length=30)
    address=models.TextField()
    email=models.EmailField(max_length=30)
    gender=models.CharField(max_length=6)
    phone=models.CharField(max_length=45)
    age=models.IntegerField()
    cityName=models.CharField(max_length=45)
    fieldSpecialist=models.TextField(default="")
    experience=models.CharField(max_length=45)

class DoctorDetails(models.Model):
    doctor=models.OneToOneField(Doctor,null=False, on_delete=models.CASCADE)
    fieldname=models.CharField(max_length=45,null=False)
    doctor_pic=models.FileField(max_length=100,upload_to="Aid_app/Doctorpic",default="")
    specialization=models.CharField(max_length=55,null=False)
    description=models.TextField(default="")
    visiting_hours=models.TextField(default="")

    