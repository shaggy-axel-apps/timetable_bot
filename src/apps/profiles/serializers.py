from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.profiles.models import Profile


User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        telegram_id = validated_data['password']
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user, telegram_id=telegram_id)
        return user
