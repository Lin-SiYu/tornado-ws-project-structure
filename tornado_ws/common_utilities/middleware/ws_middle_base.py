import importlib
from tornado.websocket import WebSocketHandler

from tornado_ws import USERS as users
from tornado_ws.config import setting


class WSMiddleware:
    def process_open(self, ws):
        pass

    def process_message(self, ws):
        pass

    def process_close(self, ws):
        pass


class WSMiddle(WebSocketHandler):
    def open(self):
        print("WSMiddle opened")
        users.add(self)
        try:
            self.middleware_list
        except AttributeError:
            self.middleware_list = setting.MIDDLEWARE_LIST
        self._middle_list_handle('process_open')

    def on_message(self, message):
        print("WSMiddle on_message")
        self.message = message
        self._middle_list_handle('process_message')
        self.msg_handle(message)

    def msg_handle(self, message):
        pass

    def on_close(self):
        print("WSMiddle closed")
        self._middle_list_handle('process_close')
        users.discard(self)

    def _middle_list_handle(self, process_func_name):
        for middleware in self.middleware_list:
            mpath, mclass = middleware.rsplit('.', maxsplit=1)
            mod = importlib.import_module(mpath)
            # getattr(mod, mclass).process_open(self, self)
            cla_obj = getattr(mod, mclass)
            func = getattr(cla_obj, process_func_name)
            func(self, self)

    # 允许所有跨域通讯，解决403问题
    def check_origin(self, origin):
        return True
