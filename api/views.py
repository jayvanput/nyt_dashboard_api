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
        days = self.request.GET.getlist('day')
        if days:
            resp = resp.filter(day__in=days)

        # Used help filter
        used_help = self.request.GET.get('used_help') or 0
        if not used_help:
            resp = resp.filter(used_help=0)

        # Date Range filter
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date') or datetime.date.today().strftime("%Y-%m-%d")
        if start_date:
            resp = resp.filter(puzzle_date__range=[start_date, end_date])
        resp = resp.order_by('-puzzle_date')
        return resp
        

    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        puzzle_date = self.request.data["puzzle_date"]
        day = datetime.datetime.strptime(puzzle_date,"%Y-%m-%d").strftime("%A")
        
        serializer.save(day=day,owner=self.request.user)