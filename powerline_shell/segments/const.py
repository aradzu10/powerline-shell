from ..utils import BasicSegment

class Segment(BasicSegment):
    def add_to_powerline(self):
        if "str" not in self.segment_def:
            return
        fg_color = self.segment_def.get("fg_color", self.powerline.theme.CONST_FG)
        bg_color = self.segment_def.get("bg_color", self.powerline.theme.CONST_BG)
        self.powerline.append(" %s " % self.segment_def["str"], fg_color, bg_color)
