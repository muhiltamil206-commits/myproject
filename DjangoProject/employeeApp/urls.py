from django.urls import path

from .import views


urlpatterns=[
    path("employee/",views.employeeview),
    path("employee/<int:id>/",views.employeeObjectView),


]