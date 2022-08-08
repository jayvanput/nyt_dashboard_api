from django.shortcuts import render
from api.serializers import EntrySerializer
from api.models import Entry

from rest_framework import viewsets

# Create your views here.
class EntryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer