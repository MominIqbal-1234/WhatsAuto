from django.contrib import admin
from weborm import models







@admin.register(models.Contacts)
class Contacts(admin.ModelAdmin):
    list_display =  ['name']


@admin.register(models.FirstTime)
class FirstTime(admin.ModelAdmin):
    list_display =  ['is_first_time']


@admin.register(models.WhatsappConnect)
class WhatsappConnect(admin.ModelAdmin):
    list_display =  ['is_login']
