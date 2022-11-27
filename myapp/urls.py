from django.urls import path

from myapp.views.home import Home

urlpatterns = [
    path("", Home.as_view(), name="myapp-home"),
]
