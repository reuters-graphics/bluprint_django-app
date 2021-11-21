import json
from pathlib import Path

from django import template
from django.conf import settings
from django.templatetags.static import static
from django.utils.safestring import mark_safe

register = template.Library()

VITE_DEV_MODE = getattr(settings, "MYAPP_VITE_DEV_MODE", False)
VITE_OUT_DIR = "vite"
APP_STATIC_DIR = "myapp"

MANIFEST_PATH = (
    Path(__file__).parent.parent / "static" / APP_STATIC_DIR / VITE_OUT_DIR / "manifest.json"
)


def get_vite_manifest():
    if not MANIFEST_PATH.exists():
        raise RuntimeError(f"Cannot find Vite manifest at {MANIFEST_PATH}")
    with MANIFEST_PATH.open() as f:
        return json.load(f)


def get_vite_asset(asset):
    manifest = get_vite_manifest()
    if asset not in manifest:
        raise RuntimeError(f"Cannot find {asset} in Vite manifest at {MANIFEST_PATH}")
    return manifest[asset]


def format_script_tag(src):
    return f'<script type="module" src="{src}"></script>'


def format_link_tag(href):
    return f'<link rel="stylesheet" href="{href}">'


def get_dev_path(asset):
    return f"/{asset}"


def get_built_path(asset):
    relative_path = f"{APP_STATIC_DIR}/{VITE_OUT_DIR}/{asset}"
    return static(relative_path)


def get_dev_scripts(asset):
    hmr = format_script_tag(get_dev_path("@vite/client"))
    app = format_script_tag(get_dev_path(asset))
    return f"{hmr}\n{app}"


def get_built_scripts(asset):
    asset_manifest = get_vite_asset(asset)
    entry = format_script_tag(get_built_path(asset_manifest["file"]))
    if "css" in asset_manifest:
        stylesheets = "\n".join(
            [format_link_tag(get_built_path(css_path)) for css_path in asset_manifest["css"]]
        )
        return f"{stylesheets}\n{entry}"
    return entry


@register.simple_tag
def vite(asset):
    if VITE_DEV_MODE:
        return mark_safe(get_dev_scripts(asset))
    return mark_safe(get_built_scripts(asset))
