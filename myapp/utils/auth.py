from django.conf import settings as project_settings
from django.contrib.auth.models import AnonymousUser
from django.utils.decorators import method_decorator
from rest_framework import authentication, exceptions

from myapp.conf import settings as app_settings
from myapp.utils.importers import import_class


def secure(view):
    """
    Authentication decorator for views.
    If DEBUG is on, we serve the view without authenticating.
    Default is 'django.contrib.auth.decorators.login_required'.
    Can also be 'django.contrib.admin.views.decorators.staff_member_required'
    or a custom decorator.
    """
    auth_decorator = import_class(app_settings.AUTH_DECORATOR)
    return (
        view if project_settings.DEBUG else method_decorator(auth_decorator, name="dispatch")(view)
    )


class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # Don't enforce if DEBUG
        if project_settings.DEBUG:
            return (AnonymousUser, None)
        try:
            # Per DRF token auth, token is prefixed by string
            # literal "Token" plus whitespace, e.g., "Token <AUTHTOKEN>"
            token = request.META.get("HTTP_AUTHORIZATION").split()[1]
        except Exception:
            raise exceptions.AuthenticationFailed("No token or incorrect token format")

        if token == app_settings.SECRET_TOKEN:
            return (AnonymousUser, None)
        raise exceptions.AuthenticationFailed("Unauthorized")
