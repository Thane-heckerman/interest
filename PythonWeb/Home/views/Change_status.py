from Home.models import StatusTracking
from django.shortcuts import render

def changeStatus(request):
    user_id = request.user.id
    user = StatusTracking.StatusTracking.objects.get(user_id = user_id )
    print(user)

    status = user.is_enabled
    print(status)
    
    if status == True:  
        print('true')
        context = {'status': 'đang tắt',
                   'action': 'bật ghi lịch sử'}
        StatusTracking.StatusTracking.objects.filter(user_id=user_id).update(is_enabled=False)
        
        
        # return HttpResponse('đã tắt')
    
    # else is_enabled == False:
    else:
        print('false')
        context = {'status': 'đang bật',
                   'action': 'tắt ghi lịch sử'}
        StatusTracking.StatusTracking.objects.filter(user_id=user_id).update(is_enabled=True)
        
        # return HttpResponse('đã bật')
    
    return render(request,'onofftracking.html', context=context)
