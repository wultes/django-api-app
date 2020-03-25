from rest_framework import serializers
from app.models import App


class AppCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('id','name', 'version')

class AppListSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('id', 'name', 'version', 'api_key')

class AppDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('id','name', 'version', 'api_key')

class AppUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('id','name', 'version', 'api_key')
        extra_kwargs = {
            'api_key': {'read_only': True}
        }
