from tornado_ws.common_utilities.middleware.ws_middle_base import WSMiddle


class TestWebSocketHandler(WSMiddle):
    # middleware_list = []
    def msg_handle(self, message):
        print(message)
