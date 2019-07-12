import logging
import time
from bson import Timestamp

from tornado_ws.common_utilities.common.dateutils import time2timestamp
from tornado_ws.common_utilities.mongo.mongo_base import mongo_handler


class OplogWatcher:
    def __init__(self, roll_time, ns):
        self.roll_time = int(roll_time)
        self.ns_filter = ns
        if '.' not in ns:
            self.ns_filter = '%s.$cmd' % ns
        self.oplog = mongo_handler.get_oplog()
        self.logger = logging.getLogger(self.__class__.__name__)

    def watcher(self):
        # 监听，调度时间间隔内的指定ns对象。
        self.logger.info('mongodb-oplog-watcher is running')
        now_timestamp = time2timestamp(time.time())
        time_offline = now_timestamp - self.roll_time
        offline_mongotime = Timestamp(time_offline, 1)
        query = {"$and": [{"ts": {"$gte": offline_mongotime}}, {"ns": {"$eq": self.ns_filter}}]}
        objs = self.oplog.find(query)
        objs_list = [obj for obj in objs]
        # print(objs_list)
        if len(objs_list) > 0:
            # todo 业务逻辑
            # 若有数据更新则根据数据_id; 操作coll无_id，操作doc有_id
            if '$cmd' in self.ns_filter:
                self.collection_handle()
            else:
                self.doc_handle()

    def collection_handle(self):
        # todo 处理操作coll的业务逻辑
        # {
        # 'ts': Timestamp(1562319727, 1),
        # 't': 5,
        # 'h': -6527299670116986509,
        # 'v': 2,
        # 'op': 'c',
        # 'ns': 'test.$cmd',
        # 'o': {'drop': 'mytest'}
        # }
        pass

    def doc_handle(self):
        # todo 操作doc的业务逻辑 - 发送 _id 对应数据给client
        # {
        # "ts" : Timestamp(1562226530, 1),
        # "t" : NumberLong(4),
        # "h" : NumberLong("4721166435781148636"),
        # "v" : 2,
        # "op" : "i",
        # "ns" : "test.testtable",
        # "o" : { "_id" : ObjectId("5d1daf5d2de6d80de8c99b7c"), "name" : "11111" }
        # }
        pass
