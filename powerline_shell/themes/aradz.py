from powerline_shell.themes import default

cyan = 51
green = 46
red = 196
faded_red = 88
normal = default.DefaultColor.RESET


class Color(default.DefaultColor):
    USERNAME_FG = green
    USERNAME_BG = 0
    USERNAME_ROOT_FG = faded_red
    USERNAME_ROOT_BG = 0

    HOSTNAME_BG = 0
    HOSTNAME_FG = green

    HOME_SPECIAL_DISPLAY = False
    HOME_BG = 0
    HOME_FG = green
    PATH_BG = 0
    PATH_FG = green
    CWD_FG = green
    SEPARATOR_FG = green

    READONLY_BG = 0
    READONLY_FG = 124

    SSH_BG = 0
    SSH_FG = 166

    REPO_CLEAN_BG = 0
    REPO_CLEAN_FG = 201
    REPO_DIRTY_BG = 0
    REPO_DIRTY_FG = 135

    JOBS_FG = 238
    JOBS_BG = 0

    CMD_PASSED_FG = green
    CMD_PASSED_BG = 0
    CMD_FAILED_FG = red
    CMD_FAILED_BG = 0

    SVN_CHANGES_FG = 148
    SVN_CHANGES_BG = 0

    GIT_AHEAD_BG = 0
    GIT_AHEAD_FG = 148
    GIT_BEHIND_BG = 0
    GIT_BEHIND_FG = 161
    GIT_STAGED_BG = 0
    GIT_STAGED_FG = 2
    GIT_NOTSTAGED_BG = 0
    GIT_NOTSTAGED_FG = 130
    GIT_UNTRACKED_BG = 0
    GIT_UNTRACKED_FG = red
    GIT_CONFLICTED_BG = 0
    GIT_CONFLICTED_FG = 9
    GIT_STASH_BG = 0
    GIT_STASH_FG = 221

    VIRTUAL_ENV_BG = 0
    VIRTUAL_ENV_FG = 35

    BATTERY_NORMAL_BG = 0
    BATTERY_NORMAL_FG = 22
    BATTERY_LOW_BG = 0
    BATTERY_LOW_FG = 196

    AWS_PROFILE_FG = 238
    AWS_PROFILE_BG = 0

    TIME_FG = cyan
    TIME_BG = 0

    CONST_FG = normal
    CONST_BG = 0
