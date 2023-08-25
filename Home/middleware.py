from typing import Any
from .models import History
from django.urls import ResolverMatch
class SearchHistory:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        ignore_urls = ['/Home/interest/', '/Home/logout/', '/Home/login/', '/Home/', '/Home/history/']
        if request.user.is_authenticated and not request.path in ignore_urls and not request.path.startswith('/Home/delete/') :
        # request.path not in ignored_urls:
            response = self.get_response(request)
            res = str(response.content).replace('b','',1)
            if hasattr(request, 'resolver_match') and isinstance(request.resolver_match, ResolverMatch):
                History.objects.create(user_id=request.user, url=request.path, period = request.resolver_match.url_name,result = res)
        # response = self.get_response(request)
            return response
        else:
            return self.get_response(request)