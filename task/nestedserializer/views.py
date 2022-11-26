import uuid

import pandas as pd
# from django.contrib.auth import get_user_model
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render
#
# # Create your views here.
# from django.utils import encoding

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.viewsets import ModelViewSet
from nestedserializer.serializers import *
from nestedserializer.models import *


class RecruiterViewSet(ModelViewSet):
    queryset = Recruiter1.objects.all()
    serializer_class = Recruiter1Serializer
    permission_classes = [AllowAny]


class CompanyViewSet(ModelViewSet):
    queryset = Company1.objects.all()
    serializer_class = Company1Serializer
    permission_classes = [AllowAny]


class SkillsViewSet(ModelViewSet):
    queryset = Skills1.objects.all()
    serializer_class = Skills1Serializer
    permission_classes = [AllowAny]


class JobViewSet(ModelViewSet):
    queryset = Job1.objects.all()
    serializer_class = Job1Serializer
    permission_classes = [AllowAny]


class Excel(APIView):
    def get(self, request, *args, **kwargs):
        job_objs = Job1.objects.all()
        serializer = Job1Serializer(job_objs, many=True)
        df = pd.DataFrame(serializer.data)
        df.to_csv(f"static/{uuid.uuid4()}.csv", encoding="UTF-8")
        return Response({'status': 200})


class ApplicantViewSet(ModelViewSet):
    queryset = Applicant1.objects.all()
    serializer_class = Applicant1Serializer
    permission_classes = [AllowAny]


class ExperienceViewSet(ModelViewSet):
    queryset = Experience1.objects.all()
    serializer_class = Experience1Serializer
    permission_classes = [AllowAny]


class QualificationViewSet(ModelViewSet):
    queryset = Qualification1.objects.all()
    serializer_class = Qualification1Serializer
    permission_classes = [AllowAny]
