from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Home.models import History
from Home.serializers.History_serializer import HistorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import json
from rest_framework.renderers import TemplateHTMLRenderer
@login_required

@api_view(['GET'])
def interest(request):
    user_id = request.user.id
    month = [0,1,2,3,4,5,6,7,8,9,10,11,12,24,36]
    queryset = History.History.objects.filter(user_id=user_id)
    serializer = HistorySerializer(queryset, many=True)
    # queryset_json = json.dumps(serializer.data)
    context = {'data': serializer.data,'month' : month}
    print(serializer.data)
    return render(request, 'home.html', context)


# request, 'home.html', {'data':data,'month':month}   .order_by('-id')[:10]