from rest_framework import viewsets
from . import models
from . import serializers


class app(viewsets.ModelViewSet):
    queryset = models.test.objects.all()
    serializer_class = serializers.app
