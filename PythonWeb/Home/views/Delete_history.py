from Home.models import History
from django.http import  HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework import viewsets
from Home.serializers.History_serializer import HistorySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import action
from django.http import HttpResponse


def delete_history(request,pk):
    if request.method == 'DELETE':
        history = History.History.objects.filter(id = pk) 
        history.delete()
        response = 'đã xoá thành công'
        return HttpResponse(response)