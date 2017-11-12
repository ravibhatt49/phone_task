from django.shortcuts import render
from rest_framework import viewsets
from accounts.models import *
from rest_framework import filters
from rest_framework import generics
from accounts.serializers import TaskSerializers, PartySerializers
import django_filters
# # from django_filters.rest_framework import DjangoFilterBackend
# from django_filters.rest_framework import DjangoFilterBackend, FilterSet


from django.db import models as django_models

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers


class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializers


# class TaskList(generics.ListAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializers
#    filter_fields = ('received_date')


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = {
            'received_date': ('lte', 'gte'),
        }

    filter_overrides = {
        django_models.DateTimeField: {
            'filter_class': django_filters.IsoDateTimeFilter
        },
    }

class TaskView(viewsets.ReadOnlyModelViewSet):
    filter_class = TaskFilter
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
# Create your views here.
