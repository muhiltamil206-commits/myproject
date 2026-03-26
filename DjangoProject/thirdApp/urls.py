

from django.urls import path
from . import views

urlpatterns = [

path('', views.profileHome, name='home'),
    path('details/', views.myDetails, name='details'),
    path('projects/', views.myProjects, name='projects'),
    path('skills/', views.mySkills, name='skills'),
    path('contact/', views.contactInfo, name='contact'),


]
