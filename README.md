# BetterLogger
#### The best option for customizable and simplicity!

## Config
All parts of the logger can be configured via environment variables.

### Required
* `"APPNAME"` - defaults to `"BetterLogger"`
* `"APPAUTHOR"` - defaults to `"BetterLogger"`
* `"APPVERSION"` - defaults to `"1.0"`
* `"SHORT_APPNAME"` - defaults to `"BL"`

### Logging Stuff
* `"LOG_LEVEL"` - defaults to `10`
* `"LOG_FORMAT"` - defaults to `"%LEVEL_COLOR[%BOLD{level: <10}]%RESET %LEVEL_COLOR[%BOLD{class_name: <32}]%RESET %LEVEL_COLOR {message}%RESET"`
* `"DISABLE_WELCOME_LOGGING"` - 
  * BetterLogger sends some welcome text to introduce the program and to test the logger
    ![welcome logging example](https://raw.githubusercontent.com/GreenJon902/BetterLogger/master/images/welcome_logging_example.png)
  * defaults to `False`
* `"LOG_WHITELIST_ON"` -
  * Turns on the log whitelist
  * Defaults to `False`
* `"LOG_WHITELIST"` -
  * Choose which log names to be allowed through
  * Defaults to `[]`
* `"LOG_BLACKLIST"` -
  * Choose which log names to be filtered out
  * Overrules values in `"LOG_WHITELIST"`
  * Defaults to `[]`
* `"LOG_NAMES_TO_SHORTEN"` -
  * An array where the key is the item that needs shortening and the value is the shortened value
  * Defaults to `{}`

### Saving Logs
* `"LOG_SAVE_DIR"` - defaults to `appdirs.user_log_dir(appname=appname, appauthor=appauthor, version=appversion)`
* `"LOG_FILE_NAME_FORMAT"` - defaults to `"{appname}_{year}-{day}-{hour}-{minute}_{number}.log"`


## Colors
BetterLogger comes with 9 colors, and 2 other text modifiers. There is black, red, green, yellow, blue, magenta, cyan, 
white, bold and reset. These can be accessed in logging by using the `%` sign and then writing the color name in all 
caps and then using the reset code, e.g. e.g. `%REDHelloWorld%Reset`
