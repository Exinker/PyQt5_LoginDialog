
import logging, logging.config
import os

with open('.env', 'r') as file:
    for line in file.readlines():
        try:
            key, value = line.strip().split('=')
            os.environ[key] = value

        except ValueError:
            pass

# database
DATABASE_HOST = os.environ['DATABASE_HOST']
DATABASE_PORT = int(os.environ['DATABASE_PORT'])

PASSWORD_PAPER = os.environ['PASSWORD_PAPER']

# logging
class FileHandler(logging.Handler):

    def __init__(self, filename, mode):
        super().__init__()

        self.filename = filename
        self.mode = mode

    def emit(self, record):
        text = self.format(record) + '\n'

        with open(self.filename, self.mode) as file:
            file.write(text)


LOGGING_CONFIG = {
    'version': 1,

    'formatters': {
        'basic': {
            'format': '%(asctime)s %(levelname)s %(message)s',
        },
    },

    'handlers': {
        'streamHandler': {
            'class': 'logging.StreamHandler',
            'level': logging.INFO,
            'formatter': 'basic',
        },
        'fileHandler': {
            '()': FileHandler,
            'filename': 'log.txt',
            'mode': 'a',
            'level': logging.INFO,
            'formatter': 'basic',
        },
    },

    'loggers': {
        'app': {
            'level': logging.INFO,
            'handlers': ['streamHandler', 'fileHandler'],
            'propagate': False,
        },
    },

}

logging.config.dictConfig(LOGGING_CONFIG)  # set logging config
