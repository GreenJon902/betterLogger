import os

os.environ["LOG_BLACKLIST"] = repr(["A.F", "C", "RootLogger"])
os.environ["LOG_LEVEL"] = "11"
os.environ["DISABLE_WELCOME_LOGGING"] = str(True)


import betterLogger
a = betterLogger.get_logger("A")
b = betterLogger.get_logger("B")
c = betterLogger.get_logger("C")

a.log_info("You should be able to see this and 2 other messages from B.F and B")
b.log_info("You should be able to see this and 2 other messages from A and B.F")
c.log_info("You shouldn't be able to see this")
a.push_logger_name("F")
a.log_info("You shouldn't be able to see this")
b.push_logger_name("F")
b.log_info("You should be able to see this and 2 other messages from A and B")
