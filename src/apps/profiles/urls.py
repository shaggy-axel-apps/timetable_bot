from django.urls import path

from apps.profiles import views


urlpatterns = [
    # path('', views.UserListView.as_view()),
    path('register/', views.UserCreateApiView.as_view(), name="register"),
]
