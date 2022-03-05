from __future__ import absolute_import
import time

from powerline_shell import utils


class Segment(utils.BasicSegment):
    def add_to_powerline(self):
        powerline = self.powerline
        format = powerline.segment_conf('time', 'format')
        if format:
            time_ = time.strftime(format)
        elif powerline.args.shell == 'bash':
            time_ = '\\t'
        elif powerline.args.shell == 'zsh':
            time_ = '%*'
        else:
            time_ = time.strftime('%H:%M:%S')
        powerline.append(time_, powerline.theme.TIME_FG,
                         powerline.theme.TIME_BG)
