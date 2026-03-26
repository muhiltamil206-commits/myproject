


from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homeContent, name='homepage'),
    path('about/', views.aboutContent, name='aboutpage'),
]