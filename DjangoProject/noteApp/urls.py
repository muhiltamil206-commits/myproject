
from django.urls import path

from .import views


urlpatterns=[
    path("personal/", views.personalForm),
    path("personalResponse/", views.personalResponse),


]
