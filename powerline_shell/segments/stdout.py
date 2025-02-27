import subprocess

from powerline_shell import utils


class Segment(utils.ThreadedSegment):
    def run(self):
        cmd = self.segment_def["command"]
        self.output = subprocess.check_output(cmd).decode("utf-8").strip()
        # TODO handle OSError
        # TODO handle no command defined or malformed

    def add_to_powerline(self):
        self.join()
        self.powerline.append(
            self.output,
            self.segment_def.get("fg_color", self.powerline.theme.PATH_FG),
            self.segment_def.get("bg_color", self.powerline.theme.PATH_BG))
