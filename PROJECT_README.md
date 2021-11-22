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

### Servers

To start developing, open TWO terminals.

In the first, navigate to the `staticapp/` directory, install dependencies and start Vite's development server.

```bash
cd staticapp
npm install
npm run start
```

In the second, change to the `example/` directory, and use the Makefile to bootstrap your Django app and start Django's development server.

```bash
cd example
make bootstrap
make develop
```

### Django Settings

#### `MYAPP_VITE_SERVER_PORT`

In `example/project/settings.py`, make sure the `MYAPP_VITE_SERVER_PORT` is set to the port the Vite server is running on. (Default, `3000`.)

#### `MYAPP_VITE_DEV_MODE`

As long as `MYAPP_VITE_DEV_MODE` is `True`, then your app's template tags will resolve to the development version of scripts served by Vite. If it is set to `False` (which is the default), the template tags will look for scripts in your app's static files directory, expecting them to have been built by Vite.

### Template tags

To add a script you're building in your Vite environment to a template, use your apps template tags and reference the script in your `staticapp/src/` directory.

```jinja
<head>
  {% load myapp_manifest %}
  {% vite_hmr %}
  {% vite 'src/home.js' %}
</head>
```

### Building scripts

Any JS file at the root of `staticapp/src/` will be considered an entry and will be served and built by Vite.

To add a new script then, add the file:

```bash
staticapp/
  src/
    home.js
    myapp.js 👈
```

Then use your template:

```jinja
<head>
  {% load myapp_manifest %}
  {% vite_hmr %}
  {% vite 'src/myapp.js' %}
</head>
```

When you're done writing your script, be sure to build it, which will put it and any other assets -- stylesheets, dynamic scripts, etc. -- in your app's static files directory.

```bash
npm run build
```
