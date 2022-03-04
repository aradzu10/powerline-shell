import getpass

from ..utils import BasicSegment


class Segment(BasicSegment):
    def add_to_powerline(self):
        powerline = self.powerline
        root_indicators = {
            'bash': '\\$',
            'tcsh': '%#',
            'zsh': '%#',
            'bare': '$',
        }
        is_root = getpass.getuser() == "root"
        indicator = root_indicators[powerline.args.shell]
        if "str" in self.segment_def and not is_root:
            indicator = self.segment_def["str"]
        bg = powerline.theme.USERNAME_BG
        fg = powerline.theme.USERNAME_FG
        if is_root:
            bg = powerline.theme.USERNAME_ROOT_BG
            fg = powerline.theme.USERNAME_ROOT_FG
        powerline.append(indicator, fg, bg, sanitize=False)
