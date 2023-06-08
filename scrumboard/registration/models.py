from django.db import models

class Users(models.Model):
    e_mail = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    time_create = models.DateTimeField(auto_now_add=True)
