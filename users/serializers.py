from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'date_of_birth', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
