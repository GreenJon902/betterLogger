import sys
from logging import StreamHandler as _StreamHandler


class ConsoleHandler(_StreamHandler):
    def __init__(self):
        _StreamHandler.__init__(self, stream=sys.stdout)


__all__ = ["ConsoleHandler"]
