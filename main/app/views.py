from django.shortcuts import render, HttpResponse
from rest_framework import generics
from django.utils.crypto import get_random_string
import json

from app.models import App
from app.serializers import AppCreateSerializer, AppListSerializer, AppDetailSerializer, AppUpdateSerializer

def appDetailJSON(request, api_key):

    app = App.objects.get(api_key=api_key)

    data = {
        'id': app.id,
        'name': app.name,
        'version': app.version,
        'api_key': app.api_key,
        'description': app.description
    }

    dump = json.dumps(data)

    return HttpResponse(dump, content_type='application/json')

def generate_key(request, id_app):

    try:
        app = App.objects.get(id=id_app)
        random_string = get_random_string(40)
        app.api_key = random_string
        app.save()

        content = {
            'message': 'Generation of a new API key is completed.',
            'id': app.id,
            'name': app.name,
            'api_key': app.api_key
        }

        dump = json.dumps(content)

        return HttpResponse(dump, content_type='application/json')
    except:
        return HttpResponse('Приложение с таким ID не существует или вы неверно ввели данные')

class AppCreateView(generics.CreateAPIView):
    serializer_class = AppCreateSerializer

class AppListView(generics.ListAPIView):
    serializer_class = AppListSerializer
    queryset = App.objects.all()

class AppDetailView(generics.RetrieveAPIView):
    serializer_class = AppDetailSerializer
    queryset = App.objects.all()

class AppUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppUpdateSerializer
    queryset = App.objects.all()


