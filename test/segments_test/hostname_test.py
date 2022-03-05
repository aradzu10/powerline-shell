from argparse import Namespace
import mock
import unittest

from powerline_shell import segments
from powerline_shell.themes import default


class HostnameTest(unittest.TestCase):
    def setUp(self):
        self.powerline = mock.MagicMock()
        self.powerline.theme = default.Color
        self.segment = segments.hostname.Segment(self.powerline, {})

    def test_colorize(self):
        self.powerline.segment_conf.return_value = True
        self.segment.start()
        self.segment.add_to_powerline()
        args = self.powerline.append.call_args[0]
        self.assertNotEqual(args[0], r" \h ")
        self.assertNotEqual(args[1], default.Color.HOSTNAME_FG)
        self.assertNotEqual(args[2], default.Color.HOSTNAME_BG)
