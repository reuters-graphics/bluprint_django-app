![](https://graphics.thomsonreuters.com/style-assets/images/logos/reuters-graphics-logo/svg/graphics-logo-color-dark.svg)

# django-myapp

## Quickstart

1. Install the app from GitHub:

   ```bash
   pipenv install -e git+https://github.com/reuters-graphics/django-myapp.git#egg=myapp
   ```

2. Add "myapp" to your INSTALLED_APPS setting like this:

   ```python
   INSTALLED_APPS = [
       # ...
       "myapp",
   ]
   ```

3. Include the myapp URLconf in your project's `urls.py` like this:

   ```python
   from django.urls import include, path

   urlpatterns = [
      # ...
      path("myapp/", include("myapp.urls")),
   ]
   ```

4. Run `python manage.py migrate` to create the myapp models.

## Developing

Read more about developing this app in the [Developing](./DEVELOPING.md) docs.
