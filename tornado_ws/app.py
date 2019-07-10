import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options

from tornado_ws.config import setting
from tornado_ws.loop_callback.beat_ping import BeatPing
from tornado_ws.urls import url_patterns


class CreatApp(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, **setting.__dict__)
        self.configure_ioloop()

    def configure_ioloop(self):
        # oplog_schedule_time = setting.OPLOG_SETTINGS['roll_time'] * 1000
        # tornado.ioloop.PeriodicCallback(OplogWatcher(**setting.OPLOG_SETTINGS).watcher,
        #                                 oplog_schedule_time).start()
        tornado.ioloop.PeriodicCallback(BeatPing(**setting.BEAT_SETTINGS).beat_ping, setting.BEAT_PING_INTERVAL).start()
        # pass


def main():
    app = CreatApp()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
