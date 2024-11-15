from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GD(models.Model):
    gd_id = models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    link = models.URLField()


class StdGD(models.Model):
    gd_id = models.ForeignKey(GD, on_delete=models.CASCADE)
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    marks = models.JSONField()