"""task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include
from rest_framework import routers

from nestedserializer.views import *

router = routers.DefaultRouter()
router.register('company1', CompanyViewSet)
router.register('recruiter1', RecruiterViewSet)
router.register('skills1', SkillsViewSet)
router.register('job1', JobViewSet)
router.register('applicant1', ApplicantViewSet)
router.register('experience1', ExperienceViewSet)
router.register('qualification1', QualificationViewSet)

urlpatterns = [

    path('', include(router.urls)),

]
