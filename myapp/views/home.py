from django.views.generic.base import TemplateView

from myapp.utils.auth import secure


@secure
class Home(TemplateView):
    template_name = "myapp/home.html"
