import logging

from tornado_ws.config import setting
from ..mq import fpika


def mq_bind(exchange, queue, exchange_type, durable=False):
    channel = fpika.channel()
    channel.exchange_declare(exchange=exchange, exchange_type=exchange_type, durable=True)
    channel.queue_declare(queue=queue, durable=durable)
    channel.queue_bind(exchange=exchange, queue=queue)


class MqName:
    def __init__(self, ex_type):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.bind_relation = setting.MQ_BIND_RELATION
        if not self.bind_relation.get(ex_type):
            # todo 错误处理
            raise Exception('Please choice the type between [fanout,dict,topic] ')
        self.ex_type = ex_type

    def bind(self):
        for queue_name, ex_name_list in self.bind_relation[self.ex_type].items():
            for ex_name in ex_name_list:
                mq_bind(ex_name, queue_name, self.ex_type)
                self.logger.info(
                    'MQ-Channel is opened,exchange:%s,queue:%s,type:%s' % (ex_name, queue_name, self.ex_type))
