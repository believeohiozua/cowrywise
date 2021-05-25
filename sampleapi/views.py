from rest_framework import views
from rest_framework.response import Response
from .serializer import UuidGeneratorSerializer
from django.http import HttpResponse
from .models import UuidGenerator
import requests


def index(request):
    return HttpResponse(requests.get('https://cowrywise.com/'))


class UuidGeneratorViews(views.APIView):
    serializer_class = UuidGeneratorSerializer

    def get(self, request, format=None):
        get_uuid = UuidGenerator.objects.values('uuid')
        get_timestamp = UuidGenerator.objects.values('timestamp').order_by('-timestamp')
        data = {}
        for key in get_timestamp:
            key = str(key.get('timestamp'))
            for value in get_uuid:
                value = str(value.get('uuid')).replace('-', '')
                data[key] = value
                break
        return Response(data)
