from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
from django.shortcuts import render
from api.serializers import EntrySerializer
from api.models import Entry
from api.permissions import IsOwnerOrReadOnly

from rest_framework import permissions
from rest_framework import viewsets

import datetime
# Create your views here.
class EntryViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            resp = Entry.objects.filter(owner=user)
        else:
            return Entry.objects.none()
        
        # Day filter
        day = self.request.GET.get('day')
        if day:
            resp = resp.filter(day=day)
        
        # Used help filter
        used_help = self.request.GET.get('used_help')
        if used_help:
            resp = resp.filter(used_help=used_help)

        # Date Range filter
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date') or datetime.date.today().strftime("%Y-%m-%d")
        print(start_date,end_date)
        if start_date:
            resp = resp.filter(puzzle_date__gte=start_date,puzzle_date__lte=end_date)

        return resp
        

    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)