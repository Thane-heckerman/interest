from Home.models import StatusTracking
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from Home.serializers.Is_enabled_seri import tracking_serializer
import json
from django.http import HttpResponse
from django.http import Http404
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics



class ToggleHistoryTrackAPIview(generics.UpdateAPIView):
    queryset = StatusTracking.StatusTracking.objects.all()
    serializer_class = tracking_serializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    

toggle_history_tracking = ToggleHistoryTrackAPIview.as_view()    
    

# from rest_framework.response import Response
# from django.core.exceptions import ObjectDoesNotExist

@api_view(['PATCH'])
def changeStatus(request, user_id, *args, **kwargs):
    user_id = request.user.id
    user = StatusTracking.StatusTracking.objects.get(user_id = user_id)
    
    serializer = tracking_serializer(user,data = request.data, partial = True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return HttpResponse('thay đổi thành công')
    
    # Update the data
    

    # if request.method == 'PATCH': 
    #     print('tới rồi đó hả')
    #     data = json.loads(request.body)
    #     user_id = request.user.id
    #     user = StatusTracking.StatusTracking.objects.get(user_id = user_id )
    #     status = user.is_enabled
        
    #     if status == True:  
            
    #         context = {'status': 'đang tắt',
    #                 'action': 'bật ghi lịch sử'}
    #         StatusTracking.StatusTracking.objects.filter(user_id=user_id).update(is_enabled=False)
            
    #     else:
            
    #         context = {'status': 'đang bật',
    #                 'action': 'tắt ghi lịch sử'}
    #         StatusTracking.StatusTracking.objects.filter(user_id=user_id).update(is_enabled=True)
            
    #         # return HttpResponse('đã bật')
    #     return HttpResponse('đã đổi')
        
        # return render(request,'onofftracking.html', context=context)
