import contextlib
import collections

from ..utils import ThreadedSegment, CustomImporter, warn


@contextlib.contextmanager
def overide_append(powerline):
    old_append = powerline.append
    try:
        yield
    finally:
        powerline.append = old_append


class Segment(ThreadedSegment):
    def __init__(self, powerline, segment_def):
        super().__init__(powerline, segment_def)
        self.segments = []

    def start(self):
        if "depend" not in self.segment_def or "segments" not in self.segment_def:
            warn("Depended group missing `depend` or `segments`")
            return
        custom_importer = CustomImporter()
        for seg_conf in self.segment_def["segments"]:
            if not isinstance(seg_conf, dict):
                seg_conf = {"type": seg_conf}
            seg_name = seg_conf["type"]
            seg_mod = custom_importer.import_(
                "powerline_shell.segments.", seg_name, "Segment")
            segment = getattr(seg_mod, "Segment")(self.powerline, seg_conf)
            segment.start()
            self.segments.append(segment)

    def add_to_powerline(self):
        appended = collections.defaultdict(list)
        with overide_append(self.powerline):
            for i, segment in enumerate(self.segments):
                def append_func(
                    content, fg, bg, separator=None, separator_fg=None, sanitize=True
                ):
                    appended[i].append((content, fg, bg, separator, separator_fg, sanitize))
                self.powerline.append = append_func
                segment.add_to_powerline()
        if len(appended) == 0:
            return
        for depend_index in self.segment_def["depend"]:
            if len(appended[depend_index]) == 0:
                return
        for i in range(len(self.segment_def["segments"])):
            for line in appended[i]:
                self.powerline.append(*line)
