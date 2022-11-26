from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db import models

# from phonenumber_field.formfields import PhoneNumberField

# Create your models here.
availability = (1, _('Not active')), (2, _('Active'))
genders = (1, _('Female')), (2, _('Male')), (3, _('prefer not to say'))
employment_type = (1, _('Full time')), (2, _('Part time'))
industry_type = ((1, "computer and IT"), (2, "management"))


class Company(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    location = models.TextField()
    date_of_start = models.DateField()
    description = models.TextField()


class Recruiter(models.Model):
    name = models.CharField(max_length=20)
    address = models.TextField()
    email = models.EmailField()
    company = models.ForeignKey(Company, default=True, on_delete=models.SET_DEFAULT)
    designation = models.CharField(max_length=30)
    bate_of_birth = models.DateField()
    gender = models.IntegerField(choices=genders, default=1)
    phone_number = models.IntegerField()


class Skill(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    # applicant = models.ManyToManyField('portal1.Skill', blank=True)


class Job(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    max_salary = models.FloatField(max_length=20)
    min_salary = models.FloatField(max_length=20)
    employment_type = models.IntegerField(choices=employment_type)
    max_experience = models.IntegerField()
    min_experience = models.IntegerField()
    company = models.ForeignKey(Company, related_name='job', default=True, on_delete=models.SET_DEFAULT)
    location = models.TextField()
    industry_type = models.IntegerField(choices=industry_type)
    date_posted = models.DateField()
    data_closed = models.DateField()
    skill = models.ManyToManyField(Skill, blank=True)
    posted_by = models.ForeignKey(User, default=True, on_delete=models.SET_DEFAULT)


class Applicant(models.Model):
    name = models.CharField(max_length=20)
    address = models.TextField()
    email = models.EmailField()
    company = models.CharField(max_length=20)
    availability = models.IntegerField(choices=availability, default=1)
    date_of_birth = models.DateField()
    gender = models.IntegerField(choices=genders, default=1)
    contact_number = models.IntegerField()
    jobs = models.ForeignKey(Job, default=True, on_delete=models.SET_DEFAULT)


class Experience(models.Model):
    project_name = models.CharField(max_length=20)
    project_description = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField()
    applicant = models.ManyToManyField(Applicant, blank=True)
    company = models.ForeignKey(Company, default=True, on_delete=models.SET_DEFAULT)


class Qualification(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    from_date = models.DateField()
    to_date = models.DateField()
    applicant = models.ForeignKey(Applicant, related_name='applicant_qualification', default=True,
                                  on_delete=models.SET_DEFAULT)
