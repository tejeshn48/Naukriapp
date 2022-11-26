from rest_framework.serializers import ModelSerializer
from .models import Company, Recruiter, Skill, Job, Applicant, Experience, Qualification


class CompanySerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Company


class RecruiterSerializer(ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        fields = '__all__'
        model = Recruiter


class ApplicantSerializer(ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        fields = '__all__'
        model = Applicant


class SkillSerializer(ModelSerializer):
    applicant = ApplicantSerializer(read_only=True)

    class Meta:
        fields = '__all__'
        model = Skill


class JobSerializer(ModelSerializer):
    company = CompanySerializer(read_only=True)
    skill = SkillSerializer(read_only=True)
    applicant = ApplicantSerializer(read_only=True)

    class Meta:
        model = Job
        fields = "__all__"


class ExperienceSerializer(ModelSerializer):
    company = CompanySerializer(read_only=True)
    applicant = ApplicantSerializer(read_only=True)

    class Meta:
        fields = '__all__'
        model = Experience


class QualificationSerializer(ModelSerializer):
    applicant = ApplicantSerializer(read_only=True)

    class Meta:
        fields = '__all__'
        model = Qualification
