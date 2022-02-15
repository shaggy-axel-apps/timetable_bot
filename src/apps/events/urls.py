from django.urls import path
from apps.events import views


urlpatterns = [
    path('', views.EventListApiView.as_view()),
    path('create/', views.EventCreateApiView.as_view()),
]
