from django.shortcuts import render

# Create your views here.


def personalForm(request):
    return render(request, "noteApp/personal.html")


# response page
def personalResponse(request):

    name = request.GET.get("name")
    age = request.GET.get("age")
    phone = request.GET.get("phone")
    email = request.GET.get("email")
    address = request.GET.get("address")

    data = {
        "name": name,
        "age": age,
        "phone": phone,
        "email": email,
        "address": address
    }

    return render(request, "noteApp/personalResponse.html", data)