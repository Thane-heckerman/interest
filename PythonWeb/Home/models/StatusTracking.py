from django.db import models
from django.contrib.auth.models import User

class StatusTracking(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_enabled = models.BooleanField(default=True, editable=True,)