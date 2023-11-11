from typing import Any
from .models import History
from django.urls import ResolverMatch
from .models import StatusTracking
import requests
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import json
class SearchHistory:
    def __init__(self,get_response):
        self.get_response = get_response


    def __call__(self, request):

        Tracking = StatusTracking.StatusTracking
        if request.user.is_authenticated:
            user = request.user.id
            try: 
                if Tracking.objects.get(user_id = user) is not None and request.path.startswith('/Home/lowest/'):
                    status = Tracking.objects.get(user_id = user)    
                    status1 = status.is_enabled
                    if status1 == True :
                        # print('đang bật chức năng lưu')
                        
                        response = self.get_response(request)
                        period = str(json.loads(request.body)) + ' tháng'
                        res = str(response.content).replace('b','',1)
                        History.History.objects.create(user=request.user, url=request.path, result = res, period=period)  
                        # print('đã ghi lịch sử')
                        return response
                            
                    else:
                        response = self.get_response(request)
                        return response
                else:
                    response = self.get_response(request)
                    return response
            except:
                
                # print('giờ không có bật chức năng lưu')
                response = self.get_response(request)
                return response
        else:
            # return self.get_response
            if request.path not in  ['/Home/','/Home/login/','/Home/logout/','/Home/register/'] :
                response = HttpResponseRedirect('/Home/')
                return response
            else:
                return self.get_response(request)

        

# period = request.resolver_match.url_name