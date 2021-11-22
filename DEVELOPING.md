![](https://graphics.thomsonreuters.com/style-assets/images/logos/reuters-graphics-logo/svg/graphics-logo-color-dark.svg)

# Developing your app

This bluprint includes a basic framework to develop a pluggable Django app with a modern frontend.

## What's in it

The project is split between three main directories:

```bash
example/
staticapp/
myapp/
```

#### `example/`

A sample Django project. Your app will be installed into this project so you can run it while developing your Django code.

#### `staticapp/`

A [Vite](https://vitejs.dev/)-based development environment. You'll develop frontend assets like JS and CSS here. It comes pre-wired for developing apps with [Svelte](https://svelte.dev/).

#### `myapp/`

Your pluggable Django app.

## Getting started

### Servers

To start developing your app, open TWO terminals.

In the first, change to the `staticapp/` directory, install dependencies and start Vite's development server.

```bash
cd staticapp
npm install
npm run start
```

In the second, change to the `example/` directory and use the Makefile to bootstrap a [pipenv](https://pipenv.pypa.io/en/latest/) virtual environment, migrate your Django database, create a superuser and start the development server.

```bash
cd example
make bootstrap
make superuser
make develop
```

### Django Settings

#### `MYAPP_VITE_SERVER_PORT`

In `example/project/settings.py`, make sure the `MYAPP_VITE_SERVER_PORT` is set to the port the Vite server is running on. (Default, `3000`.)

#### `MYAPP_VITE_DEV_MODE`

As long as `MYAPP_VITE_DEV_MODE` is `True`, then your app's template tags will resolve to the development version of scripts served by Vite. If it is set to `False` (which is the default), the template tags will look for scripts in your app's static files directory, expecting them to have been built by Vite.

### Template tags

To use a script you're building in your Vite environment within a Django template, use your app's template tags and reference the script in your `staticapp/src/` directory.

```jinja
<head>
  {% load myapp_manifest %}
  {% vite_hmr %}
  {% vite 'src/home.js' %}
</head>
```

### Building scripts

Any JS file at the root of `staticapp/src/` will be considered an entry and will be served and built by Vite.

To add a new script, create the JS entry file:

```bash
staticapp/
  src/
    home.js
    myapp.js 👈
```

... then use your template tags in one of your Django app's templates:

```jinja
<head>
  {% load myapp_manifest %}
  {% vite_hmr %}
  {% vite 'src/myapp.js' %}
</head>
```

When you're done developing your script, be sure to build it, which will put it and any other assets -- stylesheets, dynamic scripts, etc. -- in your app's static files directory.

```bash
npm run build
```

At that point, you can publish your app through pypi or GitHub.