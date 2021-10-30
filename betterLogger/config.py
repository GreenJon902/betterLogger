import os
import appdirs


def get_from_environ_else(key, if_not_exists):
    if key in os.environ:
        return os.environ.get(key)
    else:
        return if_not_exists


appname = get_from_environ_else("APPNAME", "BetterLogger")
appauthor = get_from_environ_else("APPAUTHOR", "BetterLogger")
appversion = get_from_environ_else("APPVERSION", "1.6")
short_appname = get_from_environ_else("SHORT_APPNAME", "BL")

log_level = int(get_from_environ_else("LOG_LEVEL", 10))
log_format = get_from_environ_else("LOG_FORMAT", "%LEVEL_COLOR[%BOLD{level: <10}]%RESET %LEVEL_COLOR[%BOLD{class_name: "
                                                 "<32}]%RESET %LEVEL_COLOR {message}%RESET")

save_dir = get_from_environ_else("LOG_SAVE_DIR", appdirs.user_log_dir(appname=appname, appauthor=appauthor,
                                                                      version=appversion))
save_name = get_from_environ_else("LOG_FILE_NAME_FORMAT", "{appname}_{year}-{day}-{hour}-{minute}_{number}.log")

disable_welcome_logging = bool(get_from_environ_else("DISABLE_WELCOME_LOGGING", False))

log_whitelist_on = bool(get_from_environ_else("LOG_WHITELIST_ON", False))
log_whitelist = list(eval(get_from_environ_else("LOG_WHITELIST", "[]")))
log_blacklist = list(eval(get_from_environ_else("LOG_BLACKLIST", "[]")))

log_names_to_shorten = dict(eval(get_from_environ_else("LOG_NAMES_TO_SHORTEN", "{}")))

