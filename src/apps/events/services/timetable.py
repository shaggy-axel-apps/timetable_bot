import string
from typing import Optional
from apps.events.exceptions import ValidationEventError
from apps.events.models import Event, EventTime


class UserEventManager:
    def __init__(self, user):
        self.user = user

    def event_exists(self, event_name: str) -> bool:
        return Event.objects.exists(user=self.user, title=event_name)

    def event_create(self, event_name: str) -> Event:
        return Event.objects.get_or_create(user=self.user, title=event_name)[0]

    def event_update(self, current: Optional[dict], new: Optional[dict]):
        if current and new:
            event = Event.objects.get(user=self.user, title=current['title'], color=current['color'])
            validated_data = self.validate_event_data(new)
            for field, value in validated_data.items():
                setattr(event, field, value)

    def event_time_create(self, event: Event, start_time: str, end_time: str, days: list) -> EventTime:
        event_time = EventTime.objects.get_or_create(
            event=event, start_time=start_time, end_time=end_time)
        if all([day in days for day in event_time.days.all()]):
            return event_time
        event_time.days.add(*days)
        event_time.save()
        return event_time

    def event_time_delete(self):
        pass

    def event_time_update(self):
        pass

    def validate_event_data(data: dict) -> dict:
        is_valid = []
        if 'title' in data:
            is_valid.append(isinstance(data['title'], str))
        if 'color' in data:
            is_valid.append(data['color'][0] == "#")
            is_valid.append(len(data['color']) == 7)
            is_valid += [digit in string.hexdigits for digit in data['color'][1:]]
        if is_valid:
            if all(is_valid):
                return data
            raise ValidationEventError()
