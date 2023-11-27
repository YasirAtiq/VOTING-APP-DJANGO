from django.db import models

class Votes(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField(auto_now=True)
    choice = models.CharField(max_length=80)
