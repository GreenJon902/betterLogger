import copy
from logging import Formatter as _Formatter

from betterLogger import colors
from betterLogger import config
from betterLogger.format_funcs import colored_format


class Formatter(_Formatter):
    def __init__(self, use_color=False):
        _Formatter.__init__(self)
        self.use_color = use_color

    def format(self, record):
        record = copy.deepcopy(record)

        """if record.name in constants.logging.custom_name_per_log_array.keys():
            new_name, new_msg = record.msg.split(": ", maxsplit=1)

            record.name = str(constants.logging.custom_name_per_log_array[record.name]) % new_name
            record.msg = new_msg"""  # fix this

        class_name = record.name
        for log_name, shortened in config.log_names_to_shorten.items():
            class_name = class_name.replace(log_name, shortened)

        record.msg = colored_format(config.log_format, self.use_color,
                                    custom_tags={"message": record.msg, "logger": self, "level": record.levelname,
                                                 "class_name": class_name},
                                    custom_colors={"LEVEL_COLOR": colors.level_to_code[record.levelname]})
        return _Formatter.format(self, record)


__all__ = ["Formatter"]
