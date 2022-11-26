from rest_framework.serializers import ModelSerializer
from .models import *


class CompanySerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Company


class RecruiterSerializer(ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        fields = '__all__'
        model = Recruiter


class SkillSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Skill


class UserSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ['first_name', 'last_name']


class JobSerializer(ModelSerializer):
    company = CompanySerializer(read_only=True)
    skills = SkillSerializer(read_only=True)

    class Meta:
        fields = '__all__'
        model = Job


class ApplicantSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Applicant


class ExperienceSerializer(ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        fields = '__all__'
        model = Experience


class QualificationSerializer(ModelSerializer):
    app = ApplicantSerializer(read_only=True)

    class Meta:
        fields = '__all__'
        model = Qualification
