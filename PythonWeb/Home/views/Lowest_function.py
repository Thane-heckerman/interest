from .Crawl_interests import Interest_rate
from django.http import HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def lowest(request,selectedOption):
    if request.method == "POST":
        data = json.loads(request.body)
        obj = Interest_rate()
        month_list = obj.interest_by_month()
        
        if data == 24:
            lowest = min(month_list[13].items(), key=lambda x: x[1])
            
        elif data == 36:
            lowest = min(month_list[14].items(), key=lambda x: x[1])
            
        else:
            lowest = min(month_list[data].items(), key=lambda x: x[1])

        result = str(lowest[0]) + ':' + ' ' + str(lowest[1])
        # Trả kết quả về client
        response = result
        return HttpResponse(response)