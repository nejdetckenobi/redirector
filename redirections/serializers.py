from rest_framework import serializers
from .models import Redirection


class RedirectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Redirection
        fields = ('id', 'user', 'unique_id', 'url')
