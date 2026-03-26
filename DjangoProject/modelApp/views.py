from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import CustomerModel
from . form import  CustomerForm



# Customer data-vai table-il kaata
def customerInfo(request):
    customer = CustomerModel.objects.all()
    return render(request, template_name="modelApp/customerTable.html", context={"customer": customer})

# Pudhu customer-ai register panna
def registerForm(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Information")
        return HttpResponse("<p>Invalid credentials</p>")
    form = CustomerForm
    return render(request, template_name="modelApp/registerModel.html", context={"form": form})

# Existing data-vai update panna
def updateTableForm(request, id):
    customerData = CustomerModel.objects.get(id=id)
    if request.method == "POST":
        form = CustomerModel(request.POST, instance=customerData)
        if form.is_valid():
            form.save()
            return redirect("Information")
        return HttpResponse("<p>Invalid credentials</p>")
    form = CustomerForm
    return render(request, template_name="modelApp/registerModel.html", context={"form": form})

# Data-vai delete panna
def deleteTableForm(request, id):
    customerData = CustomerModel.objects.get(id=id)
    customerData.delete()
    return redirect("Information")