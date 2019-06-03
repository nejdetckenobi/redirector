from rest_framework import serializers
from .models import Redirection


class RedirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Redirection
        fields = ('id', 'unique_id', 'url',
                  'is_active', 'is_permanent')
