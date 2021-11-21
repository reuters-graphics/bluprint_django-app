![](https://graphics.thomsonreuters.com/style-assets/images/logos/reuters-graphics-logo/svg/graphics-logo-color-dark.svg)

# django-myapp

## Quick start

1. Install the app from GitHub:

   ```bash
   pipenv install -e git+https://github.com/reuters-graphics/django-myapp.git#egg=myapp
   ```

2. Add "myapp" to your INSTALLED_APPS setting like this:

   ```python
   INSTALLED_APPS = [
       ...
       'myapp',
   ]
   ```

3. Include the myapp URLconf in your project urls.py like this:

   ```python
   path('myapp/', include('myapp.urls')),
   ```

4. Run `python manage.py migrate` to create the myapp models.
