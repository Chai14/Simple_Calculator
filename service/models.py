from django.db import models

class Service(models.Model):
    service_title = models.CharField(max_length=50)
    service_operations = models.CharField(max_length=50)
    service_des = models.TextField()

