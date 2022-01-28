from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Event(models.Model):
    """ Event - title, category and color of case """
    title = models.CharField(max_length=255)
    color = models.CharField(max_length=10, help_text="#000000", default="#000000")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'event'
        verbose_name = "Event"
        verbose_name_plural = "Events"


class WeekDay(models.Model):
    """ Short Title (Mon), Full Title (Monday) """
    title = models.CharField(max_length=3)
    description = models.CharField(max_length=20)

    class Meta:
        db_table = 'week_day'
        verbose_name = "Week Day"
        verbose_name_plural = "Week Days"


class EventTime(models.Model):
    """ Event, List of Week Days, and start-end time (hh:mm) """
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    days = models.ManyToManyField(WeekDay)
    start_time = models.CharField(max_length=5)
    end_time = models.CharField(max_length=5)

    class Meta:
        db_table = 'event_time'
        verbose_name = "Event Time"
        verbose_name_plural = "Event Time"
