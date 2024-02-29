from django.shortcuts import render
from .models import appModel

from rest_framework import generics
from .serializers import appSerializer


class dbCreate(generics.CreateAPIView):
    queryset = appModel.objects.all()
    serializer_class = appSerializer


class dbList(generics.LostAPIView):
    queryset = appModel.objects.all()
    serializer_class = appSerializer


class dbUpdate(generics.RetrieveUpdateAPIView):
    queryset = appModel.objects.all()
    serializer_class = appSerializer


class dbDelete(generics.RetrieveDestroyAPIView):
    queryset = appModel.objects.all()
    serializer_class = appSerializer
