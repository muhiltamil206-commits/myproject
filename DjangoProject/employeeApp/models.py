from django.db import models

# Create your models here.


# Create your models here.
class employeeModel(models.Model):
    employeeName = models.CharField(max_length=150)
    employeeDepartment = models.CharField(max_length=150)
    employeeYear = models.IntegerField()
    phoneNumber = models.IntegerField()
    address = models.CharField(max_length=500)
    emailAddress = models.EmailField()
    employeeType = models.CharField(max_length=150)

    def __str__(self):
        return self.employeeName



