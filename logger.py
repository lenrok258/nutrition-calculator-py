from datetime import datetime

import config


class Logger:
    def debug(self, message, *args):
        if config.DEVEL_LOG_DEBUG:
            self.__print('DEBUG', message, *args)

    def info(self, message, *args):
        self.__print('INFO', message, *args)

    def error(self, message, *args):
        self.__print('ERROR', message, *args)

    def warn(self, message, *args):
        self.__print('WARN', message, *args)

    def __print(self, level, message, *args):
        now_string = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message_formatted = message.format(*args)
        print('{0} [{1}]: {2}'.format(now_string,
                                      level,
                                      message_formatted))
