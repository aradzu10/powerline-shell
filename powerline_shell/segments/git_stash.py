import subprocess

from powerline_shell import utils


def get_stash_count():
    try:
        p = subprocess.Popen(['git', 'stash', 'list'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             env=utils.get_git_subprocess_env())
    except OSError:
        return 0

    pdata = p.communicate()
    if p.returncode != 0:
        return 0

    return pdata[0].count(b'\n')


class Segment(utils.ThreadedSegment):
    def run(self):
        self.stash_count = get_stash_count()

    def add_to_powerline(self):
        self.join()
        if not self.stash_count:
            return

        bg = self.powerline.theme.GIT_STASH_BG
        fg = self.powerline.theme.GIT_STASH_FG

        sc = self.stash_count if self.stash_count > 1 else ''
        stash_str = u'{}{}'.format(sc, utils.RepoStats.symbols['stash'])
        self.powerline.append(stash_str, fg, bg)
