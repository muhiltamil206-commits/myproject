from django.db import models

# Create your models here.




class AppointmentModel(models.Model):

    clientName = models.CharField(max_length=150)
    phoneNumber = models.IntegerField()
    appointmentDate = models.DateField()
    appointmentTime = models.TimeField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.clientName
