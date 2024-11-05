from django.db import models

class Contacts(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    class Meta:
        app_label = 'weborm'

class ServerIP(models.Model):
    ip = models.CharField(max_length=100)

    class Meta:
        app_label = 'weborm'





    