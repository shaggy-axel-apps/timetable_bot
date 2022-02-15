from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.events.models import Event
from apps.events.serializers import EventCreateSerializer, EventListSerializer
from apps.events.services.timetable import TimeTableManager


class EventListApiView(ListAPIView):
    """ Event-List Api for concrete user """
    permissions = (IsAuthenticated,)
    serializer_class = EventListSerializer

    def get(self, request):
        queryset = self.get_queryset()
        data = self.serializer_class(queryset, many=True).data
        return Response(data)
    
    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)


class EventCreateApiView(CreateAPIView):
    """ Create Event Api """
    permissions = (IsAuthenticated,)
    serializer_class = EventCreateSerializer

    def create(self, request):
        manager = TimeTableManager(user=request.user)
        event = manager.event_create(request.data['title'], request.data['color'])
        return self.serializer_class(event).data
