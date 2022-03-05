"""
We load themes that way in order to improve performance.
"""

from powerline_shell import utils


def aradz():
    from powerline_shell.themes import aradz
    return aradz.Color


def basic():
    from powerline_shell.themes import basic
    return basic.Color


def default():
    from powerline_shell.themes import default
    return default.Color


def gruvbox():
    from powerline_shell.themes import gruvbox
    return gruvbox.Color


def solarized_dark():
    from powerline_shell.themes import solarized_dark
    return solarized_dark.Color


def solarized_light():
    from powerline_shell.themes import solarized_light
    return solarized_light.Color


def washed():
    from powerline_shell.themes import washed
    return washed.Color


THEMES_NAMES = {
    "aradz": aradz,
    "basic": basic,
    "default": default,
    "gruvbox": gruvbox,
    "solarized_dark": solarized_dark,
    "solarized_light": solarized_light,
    "washed": washed,
}


def load_theme(theme_name):
    if theme_name not in THEMES_NAMES:
        utils.warn("There is no theme with name %s" % theme_name)
    return THEMES_NAMES[theme_name]()
