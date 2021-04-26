from django.shortcuts import render
from myapp.models import Room
from rest_framework import viewsets
from django.template import RequestContext
from myapp.serializers import RoomSerializer
import requests
import json

# Create your views here.
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

def home(request):
    roomstate = 'no'
    r = requests.get('http://127.0.0.1:8000/room/1/', auth=('pi', '0553156'))
    result = r.text
    output = json.loads(result)
    roomstate = output['name']

    return render(request, 'myapp/index.html',
                            {'roomstate':roomstate})
