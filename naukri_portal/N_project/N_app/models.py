from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
availabilities = ((1, _('Actively looking')), (2, _('Not actively looking')), (3, _('Offers')))
genders = ((1, _("Female")), (2, _("Male")), (3, _("Prefer not to same")))
employment_types = ((1, _("Part time")), (2, _("Full time")))
industry_types = ((1, _('Computer and IT')), (2, _('Management')), (3, _('Education')))


class Company(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    date_of_start = models.DateField()
    description = models.TextField()


class Recruiter(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField()
    email = models.EmailField(unique=True)
    phone_no = PhoneNumberField()
    company = models.ForeignKey(Company, default=True, on_delete=models.CASCADE)
    dob = models.DateField()
    designation = models.CharField(max_length=50)
    gender = models.IntegerField(choices=genders)


class Skills(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)


class Job(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    max_salary = models.FloatField()
    min_salary = models.FloatField()
    employment_type = models.IntegerField(choices=employment_types)
    max_experience = models.CharField(max_length=20)
    min_experience = models.CharField(max_length=20)
    location = models.TextField()
    skills = models.ForeignKey("Skills", on_delete=models.CASCADE)
    company = models.ForeignKey("Company", default=True, on_delete=models.CASCADE)
    industry_type = models.IntegerField(choices=industry_types)
    posted_by = models.ForeignKey(User, default=True, on_delete=models.CASCADE)


class Applicant(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    phone_no = PhoneNumberField()
    email = models.EmailField(unique=True)
    address = models.TextField()
    dob = models.DateField()
    job = models.ForeignKey("Job", default=True, on_delete=models.CASCADE)
    gender = models.IntegerField(choices=genders)
    availability = models.IntegerField(choices=availabilities, default=1)


class Experience(models.Model):
    project_name = models.CharField(max_length=20)
    project_description = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField()
    company_name = models.ForeignKey(Company, default=True, on_delete=models.CASCADE)
    applicant = models.ManyToManyField("Applicant")


class Qualification(models.Model):
    q_name = models.CharField(max_length=20)
    q_description = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField()
    applicant = models.ForeignKey("Applicant", default=True, on_delete=models.CASCADE)
