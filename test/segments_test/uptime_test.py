import unittest
import mock

from powerline_shell import segments

test_cases = {
    # linux test cases
    "00:00:00 up 1:00,  2 users,  load average: 0,00, 0,00, 0,00": "1h",
    "00:00:00 up 10:00,  2 users,  load average: 0,00, 0,00, 0,00": "10h",
    "00:00:00 up 1 days, 1:00,  2 users,  load average: 0,00, 0,00, 0,00": "1d",
    "00:00:00 up 12 days, 1:00,  2 users,  load average: 0,00, 0,00, 0,00": "12d",
    "00:00:00 up 120 days, 49 min,  2 users,  load average: 0,00, 0,00, 0,00": "120d",

    # mac test cases
    "00:00:00 up 23  3 day(s), 10:00,  2 users,  load average: 0,00, 0,00, 0,00": "3d",
}


class UptimeTest(unittest.TestCase):

    def setUp(self):
        self.powerline = mock.MagicMock()
        self.segment = segments.uptime.Segment(self.powerline, {})

    @mock.patch('subprocess.check_output')
    def test_all(self, check_output):
        for stdout, result in test_cases.items():
            check_output.return_value = stdout
            self.segment.start()
            self.segment.add_to_powerline()
            self.assertEqual(
                self.powerline.append.call_args[0][0].split()[0], result)
