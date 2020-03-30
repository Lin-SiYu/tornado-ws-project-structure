from tornado_ws.instances.http_api.mytest import MyHttp
from tornado_ws.instances.ws_api.testws import TestWebSocketHandler

url_patterns = [
    (r"/test", MyHttp),
    (r"/", TestWebSocketHandler),
]
