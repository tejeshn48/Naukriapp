from django.contrib.auth.models import User
from .models import *
from rest_framework.serializers import ModelSerializer


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class RecruiterSerializer(ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Recruiter
        fields = "__all__"


class SkillsSerializer(ModelSerializer):
    class Meta:
        model = Skills
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name")


class JobSerializer(ModelSerializer):
    skill = SkillsSerializer(read_only=True)
    company = CompanySerializer(read_only=True)
    posted_by = UserSerializer(read_only=True)

    class Meta:
        model = Job
        fields = "__all__"


class ApplicantSerializer(ModelSerializer):
    job = JobSerializer(read_only=True)
    recruiter = RecruiterSerializer(read_only=True, many=True)

    class Meta:
        model = Applicant
        fields = "__all__"


class ExperienceSerializer(ModelSerializer):
    company = CompanySerializer(read_only=True)
    applicant = ApplicantSerializer(read_only=True, many=True)

    class Meta:
        model = Experience
        fields = "__all__"


class QualificationSerializer(ModelSerializer):
    applicant = ApplicantSerializer(read_only=True)

    class Meta:
        model = Qualification
        fields = "__all__"
