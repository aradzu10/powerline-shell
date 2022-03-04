from ..utils import BasicSegment


class Segment(BasicSegment):
    def add_to_powerline(self):
        if "str" not in self.segment_def:
            warn("No `str` field inside of string exit code")
            return
        if self.powerline.args.prev_error == 0:
            fg = self.powerline.theme.CMD_PASSED_FG
            bg = self.powerline.theme.CMD_PASSED_BG
        else:
            fg = self.powerline.theme.CMD_FAILED_FG
            bg = self.powerline.theme.CMD_FAILED_BG
        self.powerline.append(str(self.segment_def["str"]), fg, bg)
