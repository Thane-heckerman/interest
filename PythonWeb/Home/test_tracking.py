
from .models.StatusTracking import StatusTracking
from .serializers.Is_enabled_seri import tracking_serializer
from rest_framework import generics, mixins
from rest_framework.response import Response

class TrackingList(generics.ListCreateAPIView):
    queryset = StatusTracking.objects.all()
    serializer_class = tracking_serializer


class TrackingDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = StatusTracking.objects.all()
    serializer_class = tracking_serializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs): 
        return self.destroy(request, *args, **kwargs)