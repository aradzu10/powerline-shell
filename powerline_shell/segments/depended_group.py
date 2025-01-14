import collections
import contextlib

from powerline_shell import utils
from powerline_shell.segments import load_segment


@contextlib.contextmanager
def overide_append(powerline):
    old_append = powerline.append
    try:
        yield
    finally:
        powerline.append = old_append


class Segment(utils.ThreadedSegment):
    def __init__(self, powerline, segment_def):
        super().__init__(powerline, segment_def)
        self.appended = collections.defaultdict(list)
        self.segments = []
        self.should_print = True

    def run(self):
        if "depend" not in self.segment_def or "segments" not in self.segment_def:
            utils.warn("Depended group missing `depend` or `segments`")
            return
        self.parse_segments()

    def parse_segments(self):
        for seg_conf in self.segment_def["segments"]:
            if not isinstance(seg_conf, dict):
                seg_conf = {"type": seg_conf}
            seg_name = seg_conf["type"]
            seg_class = load_segment.load_segment(seg_name)
            segment = seg_class(self.powerline, seg_conf)
            segment.start()
            self.segments.append(segment)

    def run_depended_on_segments(self):
        with overide_append(self.powerline):
            for i in self.segment_def["depend"]:
                segment = self.segments[i]

                def append_func(
                    content, fg, bg, separator=None, separator_fg=None, sanitize=True
                ):
                    self.appended[i].append(
                        (content, fg, bg, separator, separator_fg, sanitize))
                self.powerline.append = append_func
                segment.add_to_powerline()
        for i in self.segment_def["depend"]:
            if len(self.appended[i]) == 0:
                self.should_print = False
                return

    def add_to_powerline(self):
        self.join()
        self.run_depended_on_segments()
        if not self.should_print:
            return
        for i in range(len(self.segments)):
            if i in self.appended:
                for line in self.appended[i]:
                    self.powerline.append(*line)
            else:
                self.segments[i].add_to_powerline()
