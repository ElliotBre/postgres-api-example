from rest_framework import serializers
from .models import app


class app(serializers.ModelSerializer):
    class Meta:
        model = app
        fields = '__all__'
