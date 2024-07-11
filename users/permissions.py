from rest_framework import permissions


class IsModer(permissions.BasePermission):
    message = 'Adding customers not allowed.'

    def has_permission(self, request, view):
        return request.user.groups.filter(name='moders').exists()


class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        else:
            return False


class IsThatMe(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.pk == request.user.pk:
            return True
        else:
            return False