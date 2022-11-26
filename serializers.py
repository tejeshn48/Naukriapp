from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from .models import *


class Company1Serializer(ModelSerializer):
    class Meta:
        model = Company1
        fields = '__all__'


class Recruiter1Serializer(ModelSerializer):
    company = Company1Serializer(read_only=True)

    class Meta:
        model = Recruiter1
        fields = '__all__'


class Skills1Serializer(ModelSerializer):
    class Meta:
        model = Skills1
        fields = '__all__'


class Job1Serializer(ModelSerializer):
    skills = Skills1Serializer(read_only=True)
    company = Company1Serializer(read_only=True)

    class Meta:
        model = Job1
        fields = '__all__'


class Applicant1Serializer(ModelSerializer):
    job = Job1Serializer(read_only=True)
    recruiter = Recruiter1Serializer(read_only=True)

    class Meta:
        model = Applicant1
        fields = '__all__'


class Experience1Serializer(ModelSerializer):
    company = Company1Serializer(read_only=True)
    applicant = Applicant1Serializer(read_only=True, many=True)

    class Meta:
        model = Experience1
        fields = '__all__'


class Qualification1Serializer(ModelSerializer):
    applicant = Applicant1Serializer(read_only=True)

    class Meta:
        model = Qualification1
        fields = '__all__'
