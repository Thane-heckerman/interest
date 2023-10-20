from Home.models import History
from django.http import  HttpResponseRedirect

def delete_history(request,id):
    history = History.History.objects.filter(id = id) #pk - primary key
    history.delete()
    return HttpResponseRedirect('/Home/interest/')  