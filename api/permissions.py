from rest_framework import permissions

class IsChef(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Chefs').exists()
class IsGraphic(permissions.BasePermission):
    def has_permission(self , request , view):
        return request.user.groups.filter(name='Graphics').exists()
