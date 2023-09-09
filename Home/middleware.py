from typing import Any
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from .models import History
from django.urls import ResolverMatch
from .models import statusTracking
import requests

class SearchHistory:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        status = statusTracking.objects.filter(id=1).first()
        request.status = status
        if status.is_enabled == True:
            ignore_urls = ['/Home/interest/', '/Home/logout/', '/Home/login/', '/Home/', '/Home/history/']
            if request.user.is_authenticated and not request.path in ignore_urls and not request.path.startswith('/Home/delete/') and hasattr(request, 'resolver_match') and isinstance(request.resolver_match, ResolverMatch) :
            # request.path not in ignored_urls:
                response = self.get_response(request)
                res = str(response.content).replace('b','',1)
                History.objects.create(user_id=request.user, url=request.path, period = request.resolver_match.url_name,result = res)     
            else:
                return self.get_response(request)        
        # response = self.get_response(request)
        else:
            return self.get_response(request)
        return self.get_response(request)
    
# class CustomHeaderMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         request.META['HISTORY_TRACKS_MIDDLEWARE'] = True
#         for key, value in request.META.items():
#             print(f"{key}: {value}")
#         return self.get_response(request)

'''
problem: làm sao để lưu trữ biến global đó 
step 1: Tạo một biến is enable set default = true là biến global
step 2: tạo 1 view truyền check biến đấy là true thì chuyển thành false là false thì chuyển thành true
step 3: sừa class search history với 2 trường hợp biến là true và false '''