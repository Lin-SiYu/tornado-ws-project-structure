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

MONGO_URI = 'mongodb://localhost:27017/'
MONGO_DATABASE = 'test'
OPLOG_SETTINGS = {
    'roll_time': 2,
    'ns': 'test.testtable'  # 监听指定coll内的doc变化
    # 'ns': 'test' # 监听指定coll的变化
}

BEAT_PING_INTERVAL = 5000
BEAT_SETTINGS = {
    # 默认为True
    # 'bool_gizp': False,
}
