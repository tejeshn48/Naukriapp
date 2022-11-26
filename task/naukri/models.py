from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

# from model_utils import Choices


# Create your models here.

# activity = (1, _('Not active')), (2, _('Active'))
# genders = (1, _('Female')), (2, _('Male')), (3, _('Prefer not to say'))
# employmenttype = (1, _('Full time')), (2, _('Part time'))
# industrytype = (("1", "Computer and IT"), ("2", "Management"))

activity = ((1, "Not Active"),
            (2, "Active"))
genders = ((1, "Female"),
           (2, "Male"))
employmenttype = ((1, "Fulltime"),
                  (2, "Parttime"))
industrytype = ((1, "Computer and IT"),
                (2, "Management"))



class Company(models.Model):
    name = models.CharField(max_length=30)
    location = models.TextField()
    date_of_start = models.DateField()
    description = models.TextField()




class Recruiter(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField()
    email = models.EmailField()
    mobile_no = PhoneNumberField(blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    designation = models.TextField()
    dob = models.DateField()
    gender = models.IntegerField(choices=genders)


class Skill(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)


class Job(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    max_salary = models.FloatField(max_length=20)
    min_salary = models.FloatField(max_length=20)
    employment_type = models.IntegerField(choices=employmenttype)
    max_experience = models.IntegerField()
    min_experience = models.IntegerField()
    company = models.ManyToManyField(Company,blank=True)
    location = models.TextField()
    industry_type = models.IntegerField(choices=industrytype)


class Applicant(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField()
    email = models.EmailField()
    mobile = PhoneNumberField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    availability = models.IntegerField(choices=activity)
    dob = models.DateField(blank=True)
    gender = models.IntegerField(choices=genders)
    job = models.ManyToManyField(Job)


class Experience(models.Model):
    project_name = models.CharField(max_length=50)
    project_description = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)


class Qualification(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    from_date = models.DateField(blank=True)
    to_date = models.DateField(blank=True)
