from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class SessionYearModel(models.Model):
    id = models.AutoField(primary_key=True)
    session_start_year = models.DateField()
    session_end_year = models.DateField()
    objects = models.Manager()
    

#Overriding the Default Django Auth User and adding the One More Field(user_type)
class CustomUser(AbstractUser):
    user_type_data = ((1, 'HOD'), (2, 'Staff'), (3, 'Student'))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)

    