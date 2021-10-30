import logging
# noinspection PyUnresolvedReferences
import sys
from copy import copy
from logging import Manager

from betterLogger.classWithLogger import ClassWithLogger
from betterLogger.consoleHandler import ConsoleHandler
from betterLogger.fileHandler import FileHandler
# Setting up logger ----------------------------------------------------------------------------------------------------
from betterLogger.filter import Filter
from betterLogger.format_funcs import standard_format
from betterLogger import config
from betterLogger.formatter import Formatter

logging.TRACE = 9
logging.DUMP = 10
logging.DEBUG = 11
# noinspection PyUnresolvedReferences
logging.addLevelName(logging.TRACE, "TRACE")
# noinspection PyUnresolvedReferences
logging.addLevelName(logging.DUMP, "DUMP")


logging.addLevelName(logging.DEBUG, "DEBUG")


root_logger = logging.getLogger("RootLogger")
# noinspection PyUnresolvedReferences
root_logger.setLevel(logging.TRACE)
# noinspection PyUnresolvedReferences,PyProtectedMember
root_logger.trace = lambda message, *args, **kws: \
    root_logger._log(logging.TRACE, message, args, **kws) if root_logger.isEnabledFor(logging.TRACE) else None
# noinspection PyUnresolvedReferences,PyProtectedMember
root_logger.dump = lambda message, *args, **kws: \
    root_logger._log(logging.DUMP, message, args, **kws) if root_logger.isEnabledFor(logging.DUMP) else None

console_handler = ConsoleHandler()
file_handler = FileHandler()
# noinspection PyUnresolvedReferences
console_handler.setLevel(logging.TRACE)
# noinspection PyUnresolvedReferences
file_handler.setLevel(logging.TRACE)

# noinspection PyShadowingBuiltins
filter = Filter()

console_formatter = Formatter(use_color=True)
file_formatter = Formatter(use_color=False)
console_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)
console_handler.addFilter(filter)
file_handler.addFilter(filter)


root_logger.addHandler(console_handler)
root_logger.addHandler(file_handler)

# Set our logger to the default ----------------------------------------------------------------------------------------
# noinspection PyTypeChecker
logging.Logger.manager = Manager(root_logger)

# Testing --------------------------------------------------------------------------------------------------------------
if not config.disable_welcome_logging:
    root_logger.critical(standard_format("Welcome to {appname}"))
    root_logger.error(standard_format("Version {appversion}"))
    root_logger.warning(standard_format("Made by {appauthor}"))
    root_logger.info(f"Logger setup and saving to {file_handler.path}")
    # noinspection SpellCheckingInspection
    root_logger.debug("Idk what to put here sooo...")
    root_logger.trace(" 0 /    |  |  +---  |   |   +--+")
    root_logger.dump("/|'     +--+  +--   |   |   |  |")
    root_logger.trace("/ \\     |  |  +---  +-  +-  +--+")
    root_logger.dump("")


root_logger.info(f"Setting log level to {config.log_level}")
root_logger.setLevel(config.log_level)
# ----------------------------------------------------------------------------------------------------------------------


def get_logger(name: str) -> ClassWithLogger:
    root_logger.dump(f"Creating logger with name \"{name}\"")
    return ClassWithLogger(name)


def push_name_to_logger_name_stack(function: callable):
    def wrapper(self, *args, **kwargs):
        self.push_logger_name(function.__name__)
        result = function(self, *args, **kwargs)
        self.pop_logger_name()

        return result
    return wrapper


def reset_logger_name_stack_for_function(function: callable):
    def wrapper(self, *args, **kwargs):
        name_before = copy(self._logger_name_stack)
        self._logger_name_stack.clear()
        result = function(self, *args, **kwargs)
        self._logger_name_stack = name_before

        return result
    return wrapper


def push_name_to_logger_name_stack_custom(name: str):
    def decorator(function: callable):
        def wrapper(self, *args, **kwargs):
            self.push_logger_name(name)
            result = function(self, *args, **kwargs)
            self.pop_logger_name()

            return result
        return wrapper
    return decorator



__all__ = ["get_logger", "ClassWithLogger", "push_name_to_logger_name_stack", "reset_logger_name_stack_for_function",
           "push_name_to_logger_name_stack_custom"]
