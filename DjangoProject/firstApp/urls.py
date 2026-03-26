
from django.urls import path

from .import views


urlpatterns=[
    path('welcome/',views.welcomeScript),
    path('template/',views.templateView),
    path("studentInfo/",views.studentInfo,name="studentData"),
    path("index/<str:name>/<int:age>/",views.indexPage,name="indexInfo"),
    path("home/<str:name>/<int:age>/",views.homePage,name="homeInfo"),
    path("myTemplate/",views.myFirstTemplate,name="TemplateApp"),
    path("secondTemp/",views.secondTemplate,name="secondTemplate"),
    path("employee/",views.employeeInfo,name="emp"),
    path("personalDetails/", views.personalDetails, name="personalDetails"),

]
