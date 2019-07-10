import os
import sys

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
