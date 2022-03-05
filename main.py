#!/usr/bin/env python

from powerline_shell import powerline_shell


if __name__ == "__main__":
    try:
        powerline_shell.powerline_shell()
    except KeyboardInterrupt:
        pass
