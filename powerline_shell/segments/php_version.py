import subprocess

from powerline_shell import utils


class Segment(utils.ThreadedSegment):
    def run(self):
        self.version = None
        try:
            output = utils.decode(
                subprocess.check_output(['php', '-r', 'echo PHP_VERSION;'],
                                        stderr=subprocess.STDOUT))
            self.version = output.split('-')[0] if '-' in output else output
        except OSError:
            self.version = None

    def add_to_powerline(self):
        self.join()
        if not self.version:
            return
        # FIXME no hard-coded colors
        self.powerline.append(self.version, 15, 4)
