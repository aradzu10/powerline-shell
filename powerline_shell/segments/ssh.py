import os

from powerline_shellf import utils


class Segment(utils.BasicSegment):
    def add_to_powerline(self):
        if os.getenv('SSH_CLIENT'):
            powerline = self.powerline
            powerline.append(
                powerline.network,
                powerline.theme.SSH_FG,
                powerline.theme.SSH_BG)
