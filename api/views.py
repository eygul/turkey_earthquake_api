from .models import Quake
from .serializers import QuakeSerializer
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import filters

class QuakeGenericViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    search_fields = ['location']
    filter_backends = (filters.SearchFilter,)
    serializer_class= QuakeSerializer
    queryset = Quake.objects.all()

    @action(detail=False)
    def latest(self, request):
        latest_quake = Quake.objects.latest('date', 'time')
        serializer = self.get_serializer(latest_quake)
        return Response(serializer.data)

    @action(detail=False)
    def latest_five(self, request):
        latest_quakes = Quake.objects.order_by('-date', '-time')[:5]
        serializer = self.get_serializer(latest_quakes, many=True)
        return Response(serializer.data)
    @action(detail=False)
    def latest_ten(self, request):
        latest_quakes = Quake.objects.order_by('-date', '-time')[:10]
        serializer = self.get_serializer(latest_quakes, many=True)
        return Response(serializer.data)
    @action(detail=False)
    def latest_fifty(self, request):
        latest_quakes = Quake.objects.order_by('-date', '-time')[:50]
        serializer = self.get_serializer(latest_quakes, many=True)
        return Response(serializer.data)
    @action(detail=False)
    def latest_hundred(self, request):
        latest_quakes = Quake.objects.order_by('-date', '-time')[:100]
        serializer = self.get_serializer(latest_quakes, many=True)
        return Response(serializer.data)
    