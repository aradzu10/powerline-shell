import subprocess

from powerline_shell import utils


class Segment(utils.BasicSegment):
    def add_to_powerline(self):
        powerline = self.powerline
        try:
            p1 = subprocess.Popen(["rbenv", "local"], stdout=subprocess.PIPE)
            version = p1.communicate()[0].decode("utf-8").rstrip()
            if len(version) <= 0:
                return
            powerline.append(
                version,
                powerline.theme.VIRTUAL_ENV_FG,
                powerline.theme.VIRTUAL_ENV_BG)
        except OSError:
            return
