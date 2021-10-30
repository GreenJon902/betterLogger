from logging import Filter as _Filter

from betterLogger import config


class Filter(_Filter):
    def filter(self, record):
        return (not config.log_whitelist_on or any(record.name.startswith(name) for name in config.log_whitelist)) and \
               not any(record.name.startswith(name) for name in config.log_blacklist)
