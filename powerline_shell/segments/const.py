from ..utils import BasicSegment, warn

class Segment(BasicSegment):
    def add_to_powerline(self):
        if "str" not in self.segment_def:
            warn("No `str` field inside of const segment")
            return
        fg_color = self.segment_def.get("fg_color", self.powerline.theme.CONST_FG)
        bg_color = self.segment_def.get("bg_color", self.powerline.theme.CONST_BG)
        self.powerline.append(self.segment_def["str"], fg_color, bg_color)
