from powerline_shell import utils


class Segment(utils.BasicSegment):
    def add_to_powerline(self):
        if self.powerline.args.prev_error == 0:
            return
        fg = self.powerline.theme.CMD_FAILED_FG
        bg = self.powerline.theme.CMD_FAILED_BG
        self.powerline.append(str(self.powerline.args.prev_error), fg, bg)
