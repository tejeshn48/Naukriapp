from django.shortcuts import render

# Create your views here.
import uuid
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .models import *
from .serializer import *
import pandas as pd
from rest_framework.response import Response


# Create your views here.
class Companyviewset(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permissions_classes = [AllowAny]


class Recruiterviewset(ModelViewSet):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer
    permissions_classes = [AllowAny]


class Skillviewset(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permissions_classes = [AllowAny]


class Jobviewset(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permissions_classes = [AllowAny]


class Excel(APIView):
    def get(self, request, *args, **kwargs):
        job_objs = Job.objects.all()
        serializer = JobSerializer(job_objs, many=True)
        df = pd.DataFrame(serializer.data)
        print(df)
        df.to_csv(f"static/{uuid.uuid4()}.csv", encoding="UTF-8")
        return Response({'status': 200})


class Applicantviewset(ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    permissions_classes = [AllowAny]


class Experienceviewset(ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permissions_classes = [AllowAny]


class Qualificationviewset(ModelViewSet):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer
    permissions_classes = [AllowAny]
