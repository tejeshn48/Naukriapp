from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField


activity = ((1, "Not Active"),
            (2, "Active"))
genders = ((1, "Female"),
           (2, "Male"))
employmenttype = ((1, "Fulltime"),
                  (2, "Parttime"))
industrytype = ((1, "Computer and IT"),
                (2, "Management"))


class Company1(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    date_of_start = models.DateField()
    description = models.TextField()


class Recruiter1(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField()
    email = models.EmailField(unique=True)
    phone_num = PhoneNumberField()
    company = models.ForeignKey(Company1, default=True, on_delete=models.CASCADE)
    dob = models.DateField()
    designation = models.CharField(max_length=40)
    gender = models.IntegerField(choices=genders)


class Skills1(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()


class Job1(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    max_salary = models.FloatField()
    min_salary = models.FloatField()
    employment_type = models.IntegerField(choices=employmenttype)
    max_experience = models.CharField(max_length=30)
    min_experience = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    skills = models.ForeignKey(Skills1, default=True, on_delete=models.SET_DEFAULT)
    company = models.ForeignKey(Company1, default=True, on_delete=models.SET_DEFAULT)
    industry_type = models.IntegerField(choices=industrytype)
    posted_by = models.ForeignKey(User, default=True, on_delete=models.SET_DEFAULT)


class Applicant1(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    phone_num = PhoneNumberField()
    email = models.EmailField()
    address = models.TextField()
    dob = models.DateField()
    job = models.ForeignKey(Job1, default=True, on_delete=models.SET_DEFAULT)
    gender = models.IntegerField(choices=genders)
    availability = models.IntegerField( choices=activity)


class Experience1(models.Model):
    project_name = models.CharField(max_length=20)
    project_description = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField()
    company_name = models.ForeignKey(Company1, default=True, on_delete=models.SET_DEFAULT)
    applicant = models.ManyToManyField("Applicant1")


class Qualification1(models.Model):
    Title = models.CharField(max_length=20)
    description = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField()
    applicant = models.ForeignKey("Applicant1", default=True, on_delete=models.CASCADE)
