from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Home.models import History
@login_required
def interest(request):
    month = [0,1,2,3,4,5,6,7,8,9,10,11,12,24,36]
    user_id = request.user.id
    data = History.History.objects.all().order_by('-id').filter(user_id = user_id)[:10]
    return render(request, 'home.html', {'data':data,'month':month})