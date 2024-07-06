# crudapp/models.py
from django.db import models

class Appointment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    reason = models.CharField(max_length=100)
    appointment_date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.appointment_date}'
