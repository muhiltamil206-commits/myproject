from django.shortcuts import render

# Create your views here.

def profileHome(request):
    return render(request,'thirdApp/profileHome.html')

def myDetails(request):
    return render(request,'thirdApp/myDetails.html')

def myProjects(request):
    return render(request,'thirdApp/myProjects.html')

def mySkills(request):
    return render(request,'thirdApp/mySkills.html')

def contactInfo(request):
    return render(request,'thirdApp/contactInfo.html')

