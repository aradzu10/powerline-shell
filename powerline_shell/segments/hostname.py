from socket import gethostname

from powerline_shell import color_compliment
from powerline_shell import colortrans
from powerline_shell import utils


class Segment(utils.BasicSegment):
    def add_to_powerline(self):
        powerline = self.powerline
        if powerline.segment_conf("hostname", "colorize"):
            hostname = gethostname()
            FG, BG = color_compliment.stringToHashToColorAndOpposite(hostname)
            FG, BG = (colortrans.rgb2short(*color) for color in [FG, BG])
            host_prompt = hostname.split(".")[0]
            powerline.append(host_prompt, FG, BG)
        else:
            if powerline.args.shell == "bash":
                host_prompt = r"\h"
            elif powerline.args.shell == "zsh":
                host_prompt = "%m"
            else:
                host_prompt = gethostname().split(".")[0]
            powerline.append(
                host_prompt, powerline.theme.HOSTNAME_FG, powerline.theme.HOSTNAME_BG)
