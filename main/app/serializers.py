from rest_framework import serializers
from app.models import App


class AppCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('id','name', 'version', 'api_key', 'description')
        extra_kwargs = {
            'api_key': {'read_only': True}
        }  

class AppListSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('id', 'name', 'version', 'api_key', 'description')

class AppDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('id','name', 'version', 'api_key', 'description')

class AppUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('id','name', 'version', 'api_key', 'description')
        extra_kwargs = {
            'api_key': {'read_only': True}
        }
