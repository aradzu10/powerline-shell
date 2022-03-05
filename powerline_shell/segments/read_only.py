import os

from powerline_shell import utils


class Segment(utils.BasicSegment):
    def add_to_powerline(self):
        powerline = self.powerline
        if not os.access(powerline.cwd, os.W_OK):
            powerline.append(
                powerline.lock,
                powerline.theme.READONLY_FG,
                powerline.theme.READONLY_BG)
