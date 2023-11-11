from Home.models.StatusTracking import StatusTracking
from django.shortcuts import render
def redirectToggle(request):
    user = request.user.id
    user_id = StatusTracking.objects.get(user_id = user)
    status = user_id.is_enabled
    if status == False:
        status = 'tắt'
    else:
        status ='bật'
        
    context = {'user_id':user, 'status':status}
    return render (request, 'onofftracking.html',context)
