from email.mime import base
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'entries', views.EntryViewSet, basename='entries')

urlpatterns = [
    path('',include(router.urls))
]