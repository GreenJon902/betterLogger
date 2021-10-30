import os

os.environ["LOG_WHITELIST_ON"] = str(True)
os.environ["LOG_WHITELIST"] = repr(["A.F", "C"])
os.environ["LOG_LEVEL"] = "11"


import betterLogger
a = betterLogger.get_logger("A")
b = betterLogger.get_logger("B")
c = betterLogger.get_logger("C")

a.log_info("You shouldn't be able to see this")
b.log_info("You shouldn't be able to see this")
c.log_info("You should be able to see this and another message")
a.push_logger_name("F")
a.log_info("You should be able to see this and another message")
