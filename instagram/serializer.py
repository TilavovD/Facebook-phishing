from rest_framework import serializers

from instagram.models import InstaUser


class InstaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstaUser
        fields = '__all__'
