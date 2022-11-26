from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from phone_field import PhoneField

# Create your models here.
Choices = (("M", "Male"),
           ("F", "Female"),
           ("N", "N/A"))


class Company(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=30)
    date_of_start = models.DateField(blank=True)
    description = models.TextField(max_length=100)


class Recruiter(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    email = models.EmailField(max_length=30)
    mobile_no = PhoneField(blank=True)
    company = models.ForeignKey(Company, default=True, on_delete=models.SET_DEFAULT)
    designation = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1,choices=Choices)


class Skill(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=100)


class Job(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    max_salary = models.FloatField()
    min_salary = models.FloatField()
    employment_type = models.CharField(max_length=30)
    max_experience = models.IntegerField(default=None)
    min_experience = models.IntegerField(default=None)
    company = models.ForeignKey(Company, default=True, on_delete=models.SET_DEFAULT)
    location = models.CharField(max_length=50)
    industry_type = models.CharField(max_length=30)
    skills = models.ForeignKey(Skill, default=True, on_delete=models.SET_DEFAULT)
    Posted_by = models.ForeignKey(User, default=True, on_delete=models.SET_DEFAULT)


class Applicant(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    email = models.EmailField(max_length=30)
    mobile_no = PhoneField(blank=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=Choices, default=1)
    availability = models.CharField(max_length=60)
    jobs = models.CharField(max_length=30)


class Experience(models.Model):
    project_name = models.CharField(max_length=30)
    project_description = models.TextField(max_length=100)
    from_start = models.DateField(blank=False)
    to_end = models.DateField(blank=False)
    company = models.ForeignKey(Company, default=True, on_delete=models.SET_DEFAULT)


class Qualification(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    from_start = models.DateField()
    to_end = models.DateField()
