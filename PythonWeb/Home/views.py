
from .models.History import History
from .serializers.History_serializer import HistorySerializer
from rest_framework import generics
from rest_framework.response import Response

class HistoryList(generics.ListCreateAPIView):
    queryset = History.objects.all().filter(user_id='3')
    serializer_class = HistorySerializer


class HistoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        print('oke')
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        if request.method == 'DELETE':
            
            self.destroy(request, *args, **kwargs)
            return Response('đã xoá thành công')
        else:
            return Response('Yêu cầu không hợp lệ')
    

