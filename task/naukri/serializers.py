from rest_framework.serializers import ModelSerializer

from .models import Recruiter, Applicant, Company, Job, Skill, Experience, Qualification


class RecruiterSerializer(ModelSerializer):
    class Meta:
        model = Recruiter
        fields = '__all__'


class ApplicantSerializer(ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class ExperienceSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


class QualificationSerializer(ModelSerializer):
    class Meta:
        model = Qualification
        fields = '__all__'
