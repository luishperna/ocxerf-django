from django.db import models

class User(models.Model):
    login = models.CharField(max_length=35)
    data_de_nascimento = models.DateField()
    senha = models.CharField(max_length=8, blank=True)
