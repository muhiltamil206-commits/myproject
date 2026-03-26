from django.urls import path
from . import views

urlpatterns = [
path('info/', views.studentInfo, name="Information"),

path('register/', views.registerForm, name="Register"),

path('update/<int:id>/', views.updateTableForm, name="valueUpdate"),

path('delete/<int:id>/', views.deleteTableForm, name="valueDelete"),


]