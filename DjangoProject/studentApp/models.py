from django.db import models

# Create your models here.
class StudentModel(models.Model):
    studentName = models.CharField(max_length=150)
    studentDepartment = models.CharField(max_length=150)
    studentYear = models.IntegerField()
    phoneNumber = models.IntegerField()
    address = models.CharField(max_length=500)
    emailAddress = models.EmailField()
    studentType = models.CharField(max_length=150)

    def __str__(self):
        return self.studentName


