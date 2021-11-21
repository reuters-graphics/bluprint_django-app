![](https://graphics.thomsonreuters.com/style-assets/images/logos/reuters-graphics-logo/svg/graphics-logo-color-dark.svg)

# django-myapp

## Quick start

1. Add "myapp" to your INSTALLED_APPS setting like this:

   ```python
   INSTALLED_APPS = [
       ...
       'myapp',
   ]
   ```

2. Include the myapp URLconf in your project urls.py like this:

   ```python
   path('myapp/', include('myapp.urls')),
   ```

3. Run `python manage.py migrate` to create the myapp models.
