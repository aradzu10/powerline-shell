import os

from powerline_shell import utils


class Segment(utils.BasicSegment):
    def add_to_powerline(self):
        aws_profile = os.environ.get("AWS_PROFILE") or \
            os.environ.get("AWS_DEFAULT_PROFILE")
        if aws_profile:
            self.powerline.append("aws:%s" % os.path.basename(aws_profile),
                                  self.powerline.theme.AWS_PROFILE_FG,
                                  self.powerline.theme.AWS_PROFILE_BG)
