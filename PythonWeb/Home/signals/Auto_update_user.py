from Home.models.StatusTracking import StatusTracking
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender = User)
def auto_update(sender ,instance, created,**kwargs):
    if created:
        print('đã tạo thêm instance trong db History và HistoryTracking')
        # History.objects.create(user = instance)
        StatusTracking.objects.create(user = instance)

