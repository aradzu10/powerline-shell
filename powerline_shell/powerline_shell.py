# -*- coding: utf-8 -*-
from __future__ import print_function
import argparse
import json
import os
import re
import sys

from powerline_shell import utils
from powerline_shell.segments import load_segment
from powerline_shell.themes import load_theme


def _current_dir():
    """Returns the full current working directory as the user would have used
    in their shell (ie. without following symbolic links).

    With the introduction of Bash for Windows, we can't use the PWD environment
    variable very easily. `os.sep` for windows is `\` but the PWD variable will
    use `/`. So just always use the `os` functions for dealing with paths. This
    also is fine because the use of PWD below is done to avoid following
    symlinks, which Windows doesn't have.

    For non-Windows systems, prefer the PWD environment variable. Python's
    `os.getcwd` function follows symbolic links, which is undesirable."""
    if os.name == "nt":
        return os.getcwd()
    return os.getenv("PWD") or os.getcwd()


def get_valid_cwd():
    """Determine and check the current working directory for validity.

    Typically, an directory arises when you checkout a different branch on git
    that doesn't have this directory. When an invalid directory is found, a
    warning is printed to the screen, but the directory is still returned
    as-is, since this is what the shell considers to be the cwd."""
    try:
        cwd = _current_dir()
    except:
        utils.warn("Your current directory is invalid. If you open a ticket at " +
                   "https://github.com/milkbikis/powerline-shell/issues/new " +
                   "we would love to help fix the issue.")
        sys.stdout.write("> ")
        sys.exit(1)

    parts = cwd.split(os.sep)
    up = cwd
    while parts and not os.path.exists(up):
        parts.pop()
        up = os.sep.join(parts)
    if cwd != up:
        utils.warn("Your current directory is invalid. Lowest valid directory: "
                   + up)
    return cwd


class Powerline(object):
    symbols = {
        'compatible': {
            'lock': 'RO',
            'network': 'SSH',
            'separator': u'\u25B6',
            'separator_thin': u'\u276F'
        },
        'patched': {
            'lock': u'\uE0A2',
            'network': 'SSH',
            'separator': u'\uE0B0',
            'separator_thin': u'\uE0B1'
        },
        'flat': {
            'lock': u'\uE0A2',
            'network': 'SSH',
            'separator': '',
            'separator_thin': ''
        },
    }

    color_templates = {
        'bash': r'\[\e%s\]',
        'tcsh': r'%%{\e%s%%}',
        'zsh': '%%{%s%%}',
        'bare': '%s',
    }

    def __init__(self, args, config, theme):
        self.args = args
        self.config = config
        self.theme = theme
        self.cwd = get_valid_cwd()
        mode = config.get("mode", "patched")
        self.color_template = self.color_templates[args.shell]
        self.reset = self.color_template % '[0m'
        self.lock = Powerline.symbols[mode]['lock']
        self.network = Powerline.symbols[mode]['network']
        self.separator = Powerline.symbols[mode]['separator']
        self.separator_thin = Powerline.symbols[mode]['separator_thin']
        self.segments = []
        self.left_padding = self.config.get("left_padding", " ")
        self.right_padding = self.config.get("right_padding", " ")

    def segment_conf(self, seg_name, key, default=None):
        return self.config.get(seg_name, {}).get(key, default)

    def color(self, prefix, code):
        if code is None:
            return ''
        elif code == self.theme.RESET:
            return self.reset
        else:
            return self.color_template % ('[%s;5;%sm' % (prefix, code))

    def fgcolor(self, code):
        return self.color('38', code)

    def bgcolor(self, code):
        return self.color('48', code)

    def append(self, content, fg, bg, separator=None, separator_fg=None, sanitize=True):
        if self.args.shell == "bash" and sanitize:
            content = re.sub(r"([`$])", r"\\\1", content)
        padding_content = self.left_padding + content + self.right_padding
        self.segments.append((
            padding_content,
            fg,
            bg,
            separator if separator is not None else self.separator,
            separator_fg if separator_fg is not None else bg))

    def draw(self):
        text = (''.join(self.draw_segment(i) for i in range(len(self.segments)))
                + self.reset) + ' '
        if utils.py3:
            return text
        else:
            return text.encode('utf-8')

    def draw_segment(self, idx):
        segment = self.segments[idx]
        next_segment = self.segments[idx +
                                     1] if idx < len(self.segments)-1 else None

        return ''.join((
            self.fgcolor(segment[1]),
            self.bgcolor(segment[2]),
            segment[0],
            self.bgcolor(next_segment[2]) if next_segment else self.reset,
            self.fgcolor(segment[4]),
            segment[3]))


POTENTIAL_LOCATIONS = [
    "powerline-shell.json",
    "~/.powerline-shell.json",
    os.path.join(os.environ.get("XDG_CONFIG_HOME", "~/.config"),
                 "powerline-shell", "config.json"),
]


def get_config():
    for location in POTENTIAL_LOCATIONS:
        full = os.path.expanduser(location)
        if os.path.exists(full):
            with open(full) as f:
                try:
                    return json.loads(f.read())
                except Exception as e:
                    utils.warn(
                        "Config file ({0}) could not be decoded! Error: {1}".format(full, e))
    return DEFAULT_CONFIG


DEFAULT_CONFIG = {
    "segments": [
        'virtual_env',
        'username',
        'hostname',
        'ssh',
        'cwd',
        'git',
        'hg',
        'jobs',
        'root',
    ]
}


def powerline_shell():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--generate-config', action='store_true',
                            help='Generate the default config and print it to stdout')
    arg_parser.add_argument('--shell', action='store', default='bash',
                            help='Set this to your shell type',
                            choices=['bash', 'tcsh', 'zsh', 'bare'])
    arg_parser.add_argument('prev_error', nargs='?', type=int, default=0,
                            help='Error code returned by the last command')
    args = arg_parser.parse_args()

    if args.generate_config:
        print("Looking for a config file inside one of those location:")
        for l in POTENTIAL_LOCATIONS:
            print(l)
        print("")
        print("Default config:")
        print(json.dumps(DEFAULT_CONFIG, indent=2))
        return 0

    config = get_config()

    theme = load_theme.load_theme(config.get("theme", "default"))()

    powerline = Powerline(args, config, theme)
    segments = []
    for seg_conf in config["segments"]:
        if not isinstance(seg_conf, dict):
            seg_conf = {"type": seg_conf}
        seg_name = seg_conf["type"]
        seg_class = load_segment.load_segment(seg_name)
        segment = seg_class(powerline, seg_conf)
        segment.start()
        segments.append(segment)
    for segment in segments:
        segment.add_to_powerline()
    sys.stdout.write(powerline.draw())
    return 0
