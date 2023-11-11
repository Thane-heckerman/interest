from rest_framework import serializers
from Home.models.History import History

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['id',
                  'result',
                  'period',
                  'date',
                  'user_id',
                  'url'
                  ]