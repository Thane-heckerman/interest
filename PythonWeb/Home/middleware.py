from typing import Any
from .models import History
from django.urls import ResolverMatch
from .models import statusTracking
import requests
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

class SearchHistory:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        if request.user.is_authenticated:
            user = request.user.id
            if statusTracking.objects.get(user_id = user) is not None:
                status = statusTracking.objects.get(user_id = user)    
                status1 = status.is_enabled
                ignore_urls = ['/Home/interest/', '/Home/logout/', '/Home/login/', '/Home/', '/Home/history/','/Home/redirectToggle/','/Home/changeStatus/','']
                if status1 == True:
                    print('đang bật chức năng lưu')
                    # request.path in ignore_urls and

                    if request.path in ignore_urls:
                        # print('không được ghi lịch sử vì url trong ignore')
                        return self.get_response(request)
                    
                    else:
                        if  not request.path.startswith('/Home/delete/') : 
                            # print ('k ghi chức năng delete')
                            response = self.get_response(request)
                            period = request.resolver_match.url_name
                            res = str(response.content).replace('b','',1)
                            History.objects.create(user=request.user, url=request.path, result = res, period=period)  
                            # print('đã ghi lịch sử')
                            return response
                        
                        else:
                            # print('url có trong ignore_url nên không lưu')
                            return self.get_response(request)   
                else:
                    response = self.get_response(request)
                    return response
            else:
                statusTracking.objects.create(user_id=user)
                # print('giờ không có bật chức năng lưu')
                response = self.get_response(request)
                return response
            # return self.get_response(request)
        else:
            if request.path not in  ['/Home/','/Home/login/','/Home/logout/','/Home/register/'] :
                response = HttpResponseRedirect('/Home/')
                return response
            else:
                return self.get_response(request)

        

# period = request.resolver_match.url_name