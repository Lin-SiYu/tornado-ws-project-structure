import json
import logging

from tornado_ws.common_utilities.middleware.ws_middle_base import WSMiddleware
from tornado_ws import USER_INFOS as user_infos


class PingMiddleware(WSMiddleware):
    '''
    用于处理 ping-pong 交互
     - open 初始化用户信息
     - message 处理用户内 pong 数据
     - close 删除用户相关数据
    '''

    def process_open(self, ws):
        # print('PingMiddleware - open')
        user_infos[self] = dict(
            count=0,
            ping=None,
        )

    def process_message(self, ws):
        # print('PingMiddleware - message')
        logging.info('Ping Middleware handle message')
        msg = json.loads(ws.message)
        user_dic = user_infos.get(self)
        # print(user_dic)
        # 若pong满足条件，即重置对应user_times
        if 'pong' in msg:
            if user_dic and user_dic['ping'] == msg['pong']:
                user_infos[self]['count'] = 0

    def process_close(self, *args, **kwargs):
        # print('PingMiddleware - close')
        if user_infos.get(self):
            # 若非自然断开连接，则删除字典内信息
            user_infos.pop(self)
