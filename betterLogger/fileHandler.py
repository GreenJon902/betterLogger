import os.path
from logging import FileHandler as _FileHandler

from betterLogger import config
from betterLogger.format_funcs import standard_format


class FileHandler(_FileHandler):
    def __init__(self, encoding=None, delay=False):
        if not os.path.exists(config.save_dir):
            os.makedirs(config.save_dir)

        file_name = standard_format(config.save_name, custom_tags={"number": "{number}"})  # A rather hacky
        #                                                                                    fix
        path = os.path.join(config.save_dir, file_name)

        if "{number}" in file_name:
            n = 0
            while True:
                filename = path.replace("{number}", str(n))
                if not os.path.exists(filename):
                    break
                n += 1
                if n > 1000:  # prevent maybe flooding ?
                    raise Exception("Too many logs, remove them")

            file_name = standard_format(config.save_name, custom_tags={"number": n})
            path = os.path.join(config.save_dir, file_name)

        _FileHandler.__init__(self, path, mode="w", encoding=encoding, delay=delay)
        self.path = path


__all__ = ["FileHandler"]
