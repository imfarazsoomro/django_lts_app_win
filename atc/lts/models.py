import datetime

import django
from django.db import models
from .constants import SERVICE_STATUS_CHOICES


class ServiceRequest(models.Model):
    ref = models.IntegerField(default=0)
    title = models.CharField(max_length=200, default='')
    price = models.IntegerField(default=0.0)
    due_date = models.DateField(default=django.utils.timezone.now)
    status = models.CharField(max_length=50, choices=SERVICE_STATUS_CHOICES, default='request')

    @property
    def remaining_time(self):
        today = datetime.date.today()
        due_date = self.due_date
        delta = due_date-today
        # print("time", due_date)
        return delta.days

