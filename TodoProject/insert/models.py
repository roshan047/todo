from django.db import models

class Task(models.Model):
    heading=models.CharField(max_length=30)
    details=models.CharField(max_length=30)
    date=models.DateField()
    is_deleted=models.CharField(max_length=3)

# Create your models here.
