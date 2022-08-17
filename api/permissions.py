import typing
from rest_framework import permissions
from django.http import HttpRequest
from django.views import View

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request: HttpRequest, view: View, obj: typing.Any) -> typing.Literal[True, False]:
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user