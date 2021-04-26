from myapp.models import Room
from rest_framework import serializers

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('url', 'name')