from django.db import models

class Contacts(models.Model):
    company_name = models.CharField(max_length=100,null=True,blank=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,null=True,blank=True)
    address = models.TextField(null=True,blank=True)

    class Meta:
        app_label = 'weborm'




class WhatsappConnect(models.Model):
    is_login = models.BooleanField()

    class Meta:
        app_label = 'weborm'


class FirstTime(models.Model):
    is_first_time = models.BooleanField()

    class Meta:
        app_label = 'weborm'

    