import gzip
import json
import logging
import time

from tornado_ws import USERS, USER_INFOS


class BeatPing(object):
    def __init__(self, users=USERS, user_infos=USER_INFOS, ping=None, bool_gzip=True):
        self.users = users
        self.user_infos = user_infos
        self.bool_gizp = bool_gzip
        if not ping:
            self.ping = round(time.time() * 1000)
        else:
            self.ping = ping
        self.logger = logging.getLogger(self.__class__.__name__)

    def beat_ping(self):
        '''
        向所有用户推送ping dict，若没有 pong 返回则断开连接
        - ping值默认为13位时间戳
        - 推送数据手动 gzip 压缩
        :return: None
        '''
        self.logger.info('beat-ping is running')
        data_dic = {'ping': self.ping}
        if self.bool_gizp:
            data = self.get_gzip(data_dic)
        else:
            data = data_dic
        for user in self.users:
            user.write_message(data, binary=self.bool_gizp)
            self.user_infos[user]['ping'] = data_dic['ping']
            if self.user_infos[user]['count'] == 2:
                user.close()
                self.user_infos.pop(user)
            else:
                self.user_infos[user]['count'] += 1

    def get_gzip(self, ping_data):
        '''
        :param ping_data: {'ping': self.ping}
        :return: gzip data
        '''
        ping_json = json.dumps(ping_data)
        ping_byte = bytes(ping_json, encoding='utf-8')
        ping_gzip = gzip.compress(ping_byte)
        return ping_gzip
