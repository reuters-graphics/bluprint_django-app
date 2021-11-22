![](https://graphics.thomsonreuters.com/style-assets/images/logos/reuters-graphics-logo/svg/graphics-logo-color-dark.svg)

# bluprint_django-app

A template for pluggable Django apps.

Includes a modern frontend development environment for building static files using [Vite](https://vitejs.dev/), preconfigured for [Svelte](https://svelte.dev/).

## Quickstart

This repo is best used with [bluprint](https://github.com/reuters-graphics/bluprint), our in-house scaffolding tool.

If you haven't already, add this bluprint to your CLI.

```bash
bluprint add reuters-graphics/bluprint_django-app
```

Make a new directory and use the bluprint.

```bash
mkdir my-project && cd my-project
bluprint start
```

Otherwise, you can copy this repo and adjust the file and settings names yourself.

## Developing

Read more about developing your app in the [Developing](./DEVELOPING.md) docs.

## Credits

Vite integration inspired by [django-vite](https://github.com/MrBin99/django-vite).
