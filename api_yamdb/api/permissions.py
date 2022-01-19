from rest_framework import permissions


class IsOwnerOrModeratorOrAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif (request.method == 'PATCH' or request.method == 'DELETE') and (
            request.user.is_admin
            or request.user.is_moderator
            or obj.author == request.user
        ):
            return True
        return obj.author == request.user
