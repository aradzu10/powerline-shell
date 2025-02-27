import mock
import sh
import shutil
import tempfile
import unittest

from powerline_shell import segments
from powerline_shell import testing_utils
from powerline_shell import utils


test_cases = (
    (["unknown:", "  new-file"], utils.RepoStats(new=1)),
    (["added:", "  added-file"], utils.RepoStats(staged=1)),
    (["modified:", "  modified-file"], utils.RepoStats(changed=1)),
    (["removed:", "  removed-file"], utils.RepoStats(changed=1)),
    (["missing:", "  missing-file"], utils.RepoStats(changed=1)),
    (["renamed:", "  renamed-file"], utils.RepoStats(changed=1)),
    (["kind changed:", "  kind-changed-file"], utils.RepoStats(changed=1))
)


class BzrTest(unittest.TestCase):

    def setUp(self):
        self.powerline = mock.MagicMock()
        self.powerline.segment_conf.side_effect = testing_utils.dict_side_effect_fn({
            ("vcs", "show_symbol"): False,
        })

        self.dirname = tempfile.mkdtemp()
        sh.cd(self.dirname)
        sh.bzr("init-repo", ".")
        sh.mkdir("trunk")
        sh.cd("trunk")
        sh.bzr("init")

        self.segment = segments.bzr.Segment(self.powerline, {})

    def tearDown(self):
        shutil.rmtree(self.dirname)

    def _add_and_commit(self, filename):
        sh.touch(filename)
        sh.bzr("add", filename)
        sh.bzr("commit", "-m", "add file " + filename)

    def _checkout_new_branch(self, branch):
        sh.cd("..")
        sh.bzr("branch", "trunk", branch)
        sh.cd(branch)

    @mock.patch("powerline_shell.utils.get_PATH")
    def test_bzr_not_installed(self, get_PATH):
        get_PATH.return_value = ""  # so bzr can't be found
        self.segment.start()
        self.segment.add_to_powerline()
        self.assertEqual(self.powerline.append.call_count, 0)

    def test_non_bzr_directory(self):
        shutil.rmtree(".bzr")
        self.segment.start()
        self.segment.add_to_powerline()
        self.assertEqual(self.powerline.append.call_count, 0)

    def test_trunk(self):
        self._add_and_commit("foo")
        self.segment.start()
        self.segment.add_to_powerline()
        self.assertEqual(self.powerline.append.call_args[0][0], " trunk ")

    def test_different_branch(self):
        self._add_and_commit("foo")
        self._checkout_new_branch("bar")
        self.segment.start()
        self.segment.add_to_powerline()
        self.assertEqual(self.powerline.append.call_args[0][0], " bar ")

    @mock.patch('powerline_shell.segments.bzr._get_bzr_status')
    def test_all(self, check_output):
        for stdout, result in test_cases:
            stats = segments.bzr.parse_bzr_stats(stdout)
            self.assertEquals(result, stats)
