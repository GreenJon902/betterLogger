import os

os.environ["APPNAME"] = "TestApp"
os.environ["SHORT_APPNAME"] = "TA"
os.environ["APPVERSION"] = "12.45"
os.environ["APPAUTHOR"] = "GreenJon902"

import betterLogger
testLogger = betterLogger.get_logger("TestLogger")

testLogger.log_info("This is a test app! The app is called {appname}, it was written by {appauthor}, it's on version "
                    "{appversion} and its name can be shortened to {short_appname}.")
