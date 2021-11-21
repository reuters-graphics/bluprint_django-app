"""
Use this file to configure pluggable app settings and resolve defaults
with any overrides set in project settings.
"""

from django.conf import settings as project_settings


class Settings:
    pass


Settings.SECRET_TOKEN = getattr(project_settings, "MYAPP_SECRET_TOKEN", "SECRET")

Settings.AUTH_DECORATOR = getattr(
    project_settings,
    "MYAPP_AUTH_DECORATOR",
    "django.contrib.admin.views.decorators.staff_member_required",
)


settings = Settings
