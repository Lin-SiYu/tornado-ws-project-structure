import os
import sys
import logging.config
from tornado.options import define

possible_topdir = os.path.normpath(os.path.join(
    os.path.abspath(__file__),
    os.pardir,
    os.pardir
))
sys.path.insert(0, possible_topdir)

define("port", default=8888, help="port to listen on")

MIDDLEWARE_LIST = [
    'tornado_ws.common_utilities.middleware.pingmiddle.PingMiddleware'
]

BEAT_PING_INTERVAL = 5000
BEAT_SETTINGS = {
    # 是否进行gzip压缩，默认为True
    # 'bool_gzip': False,
}


class LogConf:
    def __init__(self):
        log_format = '[%(asctime)s] - [%(levelname)s] - %(filename)s.%(funcName)s:%(lineno)d| %(message)s'

        logfile_dir = os.path.normpath(os.path.join(
            os.path.abspath(__file__),
            os.pardir,
            os.pardir, 'logs'))
        if not os.path.exists(logfile_dir):
            os.makedirs(logfile_dir)
        logging_dic = {
            'version': 1,
            'formatters': {
                'simple': {
                    'format': log_format
                },
            },
            'filters': {},
            'handlers': {
                'info_handler':
                    {
                        'class': 'logging.handlers.RotatingFileHandler',
                        'filename': logfile_dir + '/info.log',
                        'maxBytes': 1024 * 1024 * 100,
                        'backupCount': 5,
                        'level': 'INFO',
                        'formatter': 'simple',
                        'encoding': 'utf8'
                    },
                'error_handler':
                    {
                        'class': 'logging.handlers.RotatingFileHandler',
                        'filename': logfile_dir + '/error.log',
                        'maxBytes': 1024 * 1024 * 100,
                        'backupCount': 5,
                        'level': 'ERROR',
                        'formatter': 'simple',
                        'encoding': 'utf8'
                    },
                'console_handler':
                    {
                        'class': 'logging.StreamHandler',
                        'level': 'DEBUG',
                        'formatter': 'simple'
                    }
            },
            'root': {
                'handlers': ['console_handler', 'info_handler', 'error_handler'],
                'level': logging.DEBUG,
            }
        }
        logging.config.dictConfig(logging_dic)


logconf = LogConf()
