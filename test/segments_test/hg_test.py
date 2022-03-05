import mock
import sh
import shutil
import tempfile
import unittest

from powerline_shell import segments
from powerline_shell import testing_utils
from powerline_shell import utils


test_cases = {
    "? new-file": utils.RepoStats(new=1),
    "M modified-file": utils.RepoStats(changed=1),
    "R removed-file": utils.RepoStats(changed=1),
    "! missing-file": utils.RepoStats(changed=1),
    "A added-file": utils.RepoStats(staged=1),
}


class HgTest(unittest.TestCase):

    def setUp(self):
        self.powerline = mock.MagicMock()
        self.powerline.segment_conf.side_effect = testing_utils.dict_side_effect_fn({
            ("vcs", "show_symbol"): False,
        })

        self.dirname = tempfile.mkdtemp()
        sh.cd(self.dirname)
        sh.hg("init", ".")

        self.segment = segment.hg.Segment(self.powerline, {})

    def tearDown(self):
        shutil.rmtree(self.dirname)

    def _add_and_commit(self, filename):
        sh.touch(filename)
        sh.hg("add", filename)
        sh.hg("commit", "-m", "add file " + filename)

    def _checkout_new_branch(self, branch):
        sh.hg("branch", branch)

    @mock.patch("powerline_shell.utils.get_PATH")
    def test_hg_not_installed(self, get_PATH):
        get_PATH.return_value = "" # so hg can"t be found
        self.segment.start()
        self.segment.add_to_powerline()
        self.assertEqual(self.powerline.append.call_count, 0)

    def test_non_hg_directory(self):
        shutil.rmtree(".hg")
        self.segment.start()
        self.segment.add_to_powerline()
        self.assertEqual(self.powerline.append.call_count, 0)

    def test_standard(self):
        self._add_and_commit("foo")
        self.segment.start()
        self.segment.add_to_powerline()
        self.assertEqual(self.powerline.append.call_args[0][0], " default ")

    def test_different_branch(self):
        self._add_and_commit("foo")
        self._checkout_new_branch("bar")
        self.segment.start()
        self.segment.add_to_powerline()
        self.assertEqual(self.powerline.append.call_args[0][0], " bar ")

    @mock.patch('powerline_shell.segments.hg._get_hg_status')
    def test_all(self, check_output):
        for stdout, result in test_cases.items():
            stats = segment.hg.parse_hg_stats([stdout])
            self.assertEquals(result, stats)
