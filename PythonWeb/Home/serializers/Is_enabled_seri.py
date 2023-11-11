from rest_framework import serializers
from Home.models.StatusTracking import StatusTracking

class tracking_serializer(serializers.ModelSerializer):
    class Meta:
        model = StatusTracking
        fields = '__all__'