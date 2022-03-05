from powerline_shell import utils


class Segment(utils.BasicSegment):
    def add_to_powerline(self):
        if self.powerline.args.shell == "tcsh":
            utils.warn("newline segment not supported for tcsh (yet?)")
            return
        self.powerline.append(
            "\n", self.powerline.theme.RESET, self.powerline.theme.RESET, separator="")
