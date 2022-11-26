from django.urls import path,include
from rest_framework import routers
from .views import *

routers = routers.DefaultRouter()
routers.register(r'Company', Companyviewset,basename='Compeny')
routers.register(r'Recruiter', Recruiterviewset, basename='Recruiter')
routers.register(r'Skill', Skillviewset, basename='Skill')
routers.register(r'Job', Jobviewset, basename='Job')
routers.register(r'Applicant', Applicantviewset,basename='Applicant')
routers.register(r'Experience', Experienceviewset, basename='Experience')
routers.register(r'Qualification', Qualificationviewset, basename='Qualification')

urlpatterns = [
    path('',include(routers.urls))
]