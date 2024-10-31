from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Projeto(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=255)
    integrantes = models.ManyToManyField(User)

class Sprint(models.Model):
    Projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    numero_sprint = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=255)