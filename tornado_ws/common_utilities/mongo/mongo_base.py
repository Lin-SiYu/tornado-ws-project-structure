import logging

from pymongo import MongoClient

from tornado_ws.config import setting

logger = logging.getLogger(__name__)


class MongoHandler:

    def __init__(self, uri=None, db=None):
        try:
            if not uri:
                self.uri = setting.MONGO_URI
            self.conn = MongoClient(self.uri, connect=True, serverSelectionTimeoutMS=3000)
            logger.info('Mongodb connected ! ')
            if not db:
                self.db = self.conn.get_database(setting.MONGO_DATABASE)
            else:
                self.db = self.conn.get_database(db)
        except AttributeError as e:
            logger.error(e)

    def get_oplog(self):
        return self.conn.local.oplog.rs


mongo_handler = MongoHandler()
