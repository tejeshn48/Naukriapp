from django.contrib.auth.models import User
from django.db import models
from location_field.forms.plain import PlainLocationField
from phonenumber_field.modelfields import PhoneNumberField
# from rest_framework.authtoken.admin import User

# Create your models here.
Choices = (("M", "M"),
           ("F", "F"),
           ("N", "N"))


class Company(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    date_of_start = models.DateField(max_length=10)
    description = models.TextField(max_length=100)


class Recruiter(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    email = models.EmailField(max_length=30)
    mobile_no = PhoneNumberField()
    company = models.ForeignKey(Company,default=True,on_delete=models.SET_DEFAULT)
    designation = models.CharField(max_length=20)
    date_of_birth = models.DateField(max_length=10)
    gender = models.CharField(max_length=10, choices=Choices, default=1)


class Applicant(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    email = models.EmailField(max_length=30)
    mobile_no = PhoneNumberField()
    date_of_birth = models.DateField(max_length=10)
    gender = models.CharField(max_length=1, choices=Choices, default=1)
    availability = models.CharField(max_length=10)
    jobs = models.CharField(max_length=30)
    company = models.ForeignKey(Company, default=True,on_delete=models.SET_DEFAULT)


class Skill(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    applicant = models.ForeignKey(Applicant,default=True,on_delete=models.SET_DEFAULT)


class Job(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    max_salary = models.FloatField()
    min_salary = models.FloatField()
    employment_type = models.CharField(max_length=20)
    max_experience = models.IntegerField()
    min_experience = models.IntegerField()
    company = models.ForeignKey(Company,default=True,on_delete=models.SET_DEFAULT)
    location = models.CharField(max_length=50)
    industry_type = models.CharField(max_length=20)
    skills = models.ForeignKey(Skill,default=True,on_delete=models.SET_DEFAULT)
    applicant = models.ForeignKey(Applicant,default=True,on_delete=models.SET_DEFAULT)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Experience(models.Model):
    project_name = models.CharField(max_length=20)
    project_description = models.TextField(max_length=100)
    from_start = models.DateField(max_length=10)
    to_end = models.DateField(max_length=10)
    company = models.ForeignKey(Company,default=True,on_delete=models.SET_DEFAULT)



class Qualification(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    from_start = models.DateField(max_length=10)
    to_end = models.DateField(max_length=10)
    applicant = models.ForeignKey(Applicant,default=True,on_delete=models.SET_DEFAULT)