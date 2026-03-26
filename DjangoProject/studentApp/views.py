from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import StudentModel
from .form import StudentForm


# Student data table-il kaata
def studentInfo(request):
    student = StudentModel.objects.all()
    return render(request, template_name="studentApp/studentTable.html", context={"student": student})


# Pudhu student-ai register panna
def registerForm(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Information")
        return HttpResponse("<p>Invalid credentials</p>")
    form = StudentForm()
    return render(request, template_name="studentApp/registerModel.html", context={"form": form})


# Existing data-vai update panna
def updateTableForm(request, id):
    studentData = StudentModel.objects.get(id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=studentData)
        if form.is_valid():
            form.save()
            return redirect("Information")
        return HttpResponse("<p>Invalid credentials</p>")

    form = StudentForm(instance=studentData)

    return render(request, template_name="studentApp/registerModel.html", context={"form": form})


# Data-vai delete panna
def deleteTableForm(request, id):
    studentData = StudentModel.objects.get(id=id)
    studentData.delete()
    return redirect("Information")