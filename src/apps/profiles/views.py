from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from apps.profiles.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


class UserCreateApiView(CreateAPIView):
    """ API-Представление регистрации """
    permission_classes = (AllowAny,)
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
