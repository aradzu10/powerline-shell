"""
We load segments that way in order to improve performance.
"""

from powerline_shell import utils


def aws_profile():
    from powerline_shell.segments import aws_profile
    return aws_profile.Segment


def battery():
    from powerline_shell.segments import battery
    return battery.Segment


def bzr():
    from powerline_shell.segments import bzr
    return bzr.Segment


def const():
    from powerline_shell.segments import const
    return const.Segment


def cwd():
    from powerline_shell.segments import cwd
    return cwd.Segment


def depended_group():
    from powerline_shell.segments import depended_group
    return depended_group.Segment


def env():
    from powerline_shell.segments import env
    return env.Segment


def exit_code():
    from powerline_shell.segments import exit_code
    return exit_code.Segment


def fossil():
    from powerline_shell.segments import fossil
    return fossil.Segment


def git():
    from powerline_shell.segments import git
    return git.Segment


def git_stash():
    from powerline_shell.segments import git_stash
    return git_stash.Segment


def hg():
    from powerline_shell.segments import hg
    return hg.Segment


def hostname():
    from powerline_shell.segments import hostname
    return hostname.Segment


def jobs():
    from powerline_shell.segments import jobs
    return jobs.Segment


def last():
    from powerline_shell.segments import last
    return last.Segment


def newline():
    from powerline_shell.segments import newline
    return newline.Segment


def node_version():
    from powerline_shell.segments import node_version
    return node_version.Segment


def npm_version():
    from powerline_shell.segments import npm_version
    return npm_version.Segment


def php_version():
    from powerline_shell.segments import php_version
    return php_version.Segment


def rbenv():
    from powerline_shell.segments import rbenv
    return rbenv.Segment


def read_only():
    from powerline_shell.segments import read_only
    return read_only.Segment


def root():
    from powerline_shell.segments import root
    return root.Segment


def ruby_version():
    from powerline_shell.segments import ruby_version
    return ruby_version.Segment


def set_term_title():
    from powerline_shell.segments import set_term_title
    return set_term_title.Segment


def ssh():
    from powerline_shell.segments import ssh
    return ssh.Segment


def stdout():
    from powerline_shell.segments import stdout
    return stdout.Segment


def string_exit_code():
    from powerline_shell.segments import string_exit_code
    return string_exit_code.Segment


def svn():
    from powerline_shell.segments import svn
    return svn.Segment


def time():
    from powerline_shell.segments import time
    return time.Segment


def uptime():
    from powerline_shell.segments import uptime
    return uptime.Segment


def username():
    from powerline_shell.segments import username
    return username.Segment


def virtual_env():
    from powerline_shell.segments import virtual_env
    return virtual_env.Segment


SEGMENTS_NAMES = {
    "aws_profile": aws_profile,
    "battery": battery,
    "bzr": bzr,
    "const": const,
    "cwd": cwd,
    "depended_group": depended_group,
    "env": env,
    "exit_code": exit_code,
    "fossil": fossil,
    "git": git,
    "git_stash": git_stash,
    "hg": hg,
    "hostname": hostname,
    "jobs": jobs,
    "last": last,
    "newline": newline,
    "node_version": node_version,
    "npm_version": npm_version,
    "php_version": php_version,
    "rbenv": rbenv,
    "read_only": read_only,
    "root": root,
    "ruby_version": ruby_version,
    "set_term_title": set_term_title,
    "ssh": ssh,
    "stdout": stdout,
    "string_exit_code": string_exit_code,
    "svn": svn,
    "time": time,
    "uptime": uptime,
    "username": username,
    "virtual_env": virtual_env,
}


def load_segment(segment_name):
    if segment_name not in SEGMENTS_NAMES:
        utils.warn("There is no segment with name %s" % segment_name)
    return SEGMENTS_NAMES[segment_name]()
