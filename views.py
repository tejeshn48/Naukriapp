# from django.shortcuts import render
import uuid

import pandas as pd
from django.db.migrations import serializer
# Create your views here.

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.viewsets import ModelViewSet

from .models import *
from .serialzers import *


# Create your views here.


class RecruiterView(viewsets.ModelViewSet):
    queryset = Recruiter.objects.all()
    serializer_class = Recruiter_Serialzers


class ApplicantView(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = Applicant_Serialzers


class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = Company_Serialzers


class JobView(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = Job_Serialzers


class SkillView(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = Skill_Serialzers


class ExperienceView(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = Experience_Serialzers


class QualificationView(viewsets.ModelViewSet):
    queryset = Qualification.objects.all()
    serializer_class = Qualification_Serialzers


class Excel(APIView):
    def get(self, request, *args, **kwargs):
        Job_obj = Job.objects.all()
        serializers = Job_Serialzers(Job_obj, many=True)
        df = pd.DataFrame(serializers.data)
        print(df)
        df.to_csv(f"static/{uuid.uuid4()}.csv", encoding="UTF-8")
        return Response({'status': 200})
