#!/usr/bin/env python

try:
    from powerline_shell import powerline_shell
    if __name__ == "__main__":
        powerline_shell.powerline_shell()
except KeyboardInterrupt:
    pass
except Exception as e:
    from powerline_shell import utils
    utils.warn(e)
