import { defineConfig } from 'vite';
import glob from 'glob';
import { svelte } from '@sveltejs/vite-plugin-svelte';
import sveltePreprocess from 'svelte-preprocess';

const DJANGO_DEV_SERVER = 'http://localhost:8000';

// Entries are any JS files at root of src/
input = {};
const entries = glob.sync('src/*.js', { cwd: __dirname });
for (const entry of entries) {
  const appName = entry.match(/src\/(?<entryName>.*)\.js/);
  input[appName.groups.entryName] = entry;
}

export default defineConfig({
  build: {
    manifest: true,
    outDir: '../myapp/static/myapp/vite/',
    emptyOutDir: true,
    rollupOptions: { input },
  },
  server: {
    open: '/django/myapp/',
    proxy: {
      '/django':  {
        target: DJANGO_DEV_SERVER,
        rewrite: (path) => path.replace(/^\/django/, '')
      },
    },
  },
  plugins: [
		svelte({
      preprocess: [
        sveltePreprocess({
          preserve: ['ld+json'],
          scss: {
            includePaths: ['src/', 'node_modules/bootstrap/scss/'],
            importer: [
              (url) => /^~/.test(url) ?
                  { file: `node_modules/${url.replace('~', '')}` } : null,
            ],
            quietDeps: true,
          },
        })
      ]
    })
	],
  optimizeDeps: {
    exclude: ['svelte-fa'],
    include: [
      'marked',
      'lodash-es',
      '@reuters-graphics/graphics-svelte-components',
    ],
  },
});
