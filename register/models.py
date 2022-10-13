from django.db import models

# Create your models here.


class employee(models.Model):
    name = models.CharField(max_length=122)
    department = models.CharField(max_length=122)
