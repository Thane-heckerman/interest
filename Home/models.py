from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class History(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, blank=True , null=True)
    result = models.CharField(max_length=5, blank=True , null=True)
    period = models.CharField(max_length=100,  blank=True , null=True)  
    url = models.URLField(max_length=200)
    date = models.DateField(auto_now=True)
    
    def __unicode__(self):
        return self.period
        
class statusTracking(models.Model):
    is_enabled = models.BooleanField(default=True, editable=True,)