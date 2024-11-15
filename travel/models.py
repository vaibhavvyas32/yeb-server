from django.db import models
from django.contrib.auth.models import User


class Travel(models.Model):
    t_id = models.AutoField(primary_key=True)
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    yeb_event = models.CharField(max_length=255)
    from_location = models.CharField(max_length=255)
    to_location = models.CharField(max_length=255)
    pickup = models.CharField(max_length=255)
    drop = models.CharField(max_length=255)
    amount = models.IntegerField()
    staff = models.CharField(max_length=255)
    instructions = models.TextField()

class UTravel(models.Model):
    u_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    t_id = models.ForeignKey(Travel, on_delete=models.CASCADE)