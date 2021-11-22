![](https://graphics.thomsonreuters.com/style-assets/images/logos/reuters-graphics-logo/svg/graphics-logo-color-dark.svg)

# bluprint_django-app

A bluprint for building pluggable Django apps.

Includes a modern frontend development environment for building static files using [Vite](https://vitejs.dev/), preconfigured for [Svelte](https://svelte.dev/).

## Quickstart

This rig is best used with [bluprint](https://github.com/reuters-graphics/bluprint), our in-house templating tool.

If you haven't already, add this bluprint to your CLI.

```bash
bluprint add reuters-graphics/bluprint_django-app
```

Make a new directory and use the bluprint.

```bash
mkdir my-project && cd my-project
bluprint start
```

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

#### `<YOURAPP>_VITE_SERVER_PORT`

In `example/project/settings.py`, make sure the `<YOURAPP>_VITE_SERVER_PORT` is set to the port the Vite server is running on. (Default, `3000`.)

#### `<YOURAPP>_VITE_DEV_MODE`

As long as `<YOURAPP>_VITE_DEV_MODE` is `True`, then your app's template tags will resolve to the development version of scripts served by Vite. If it is set to `False` (which is the default), the template tags will look for scripts in your app's static files directory, expecting them to have been built by Vite.

### Template tags

To add a script you're building in your Vite environment to a template, use your apps template tags and reference the script in your `staticapp/src/` directory.

```jinja
<head>
  {% load <yourapp>_manifest %}
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
  {% load <yourapp>_manifest %}
  {% vite_hmr %}
  {% vite 'src/myapp.js' %}
</head>
```

When you're done writing your script, be sure to build it, which will put it and any other assets -- stylesheets, dynamic scripts, etc. -- in your app's static files directory.

```bash
npm run build
```
