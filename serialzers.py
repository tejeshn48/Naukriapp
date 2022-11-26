from rest_framework import serializers
from .models import *


class Company_Serialzers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class Skill_Serialzers(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class Recruiter_Serialzers(serializers.ModelSerializer):
    company = Company_Serialzers(read_only=True)

    class Meta:
        model = Recruiter
        fields = '__all__'


class Job_Serialzers(serializers.ModelSerializer):
    company = Company_Serialzers(read_only=True)
    skill = Skill_Serialzers(read_only=True, many=True)

    class Meta:
        model = Job
        fields = ("__all__")


class Applicant_Serialzers(serializers.ModelSerializer):
    job = Job_Serialzers(read_only=True, many=True)

    class Meta:
        model = Applicant
        fields = '__all__'


class Experience_Serialzers(serializers.ModelSerializer):
    applicant = Applicant_Serialzers(read_only=True, many=True)
    company = Company_Serialzers(read_only=True)

    class Meta:
        model = Experience
        fields = '__all__'


class Qualification_Serialzers(serializers.ModelSerializer):
    applicant = Applicant_Serialzers(read_only=True)

    class Meta:
        model = Qualification
        fields = '__all__'
