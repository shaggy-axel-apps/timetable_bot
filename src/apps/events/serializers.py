from rest_framework.serializers import ModelSerializer

from apps.events.models import Event


class EventListSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'color')


class EventCreateSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'color')
