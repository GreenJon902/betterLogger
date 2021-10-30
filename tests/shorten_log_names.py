import os

os.environ["LOG_NAMES_TO_SHORTEN"] = repr({"AnExtremelyLongLoggerName": "AELLN",
                                           "AnExtremelyLongLoggerSubName": "AELLSN"})

import betterLogger
long = betterLogger.get_logger("AnExtremelyLongLoggerName")
long_sub_name = betterLogger.get_logger("Logger.AnExtremelyLongLoggerSubName")

long.log_info("This messages class name should be AELLN which stands for AnExtremelyLongLoggerName")
long_sub_name.log_info("This messages class name should be Logger.AELLSN which stands for "
                       "Logger.AnExtremelyLongLoggerSubName")
long.push_logger_name("AnExtremelyLongLoggerSubName")
long.log_info("This messages class name should be AELLN.AELLSN which stands for "
              "AnExtremelyLongLoggerName.AnExtremelyLongLoggerSubName")
