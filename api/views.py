from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
from django.shortcuts import render
from api.serializers import EntrySerializer
from api.models import Entry
from api.permissions import IsOwnerOrReadOnly

from rest_framework import permissions
from rest_framework import viewsets

# Create your views here.
class EntryViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            return Entry.objects.filter(owner=user)
        else:
            return Entry.objects.none()

    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)