from django.db import models

# Create your models here.
class post(models.Model):
    text = models.CharField(max_length=480)