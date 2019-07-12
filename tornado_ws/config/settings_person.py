MONGO_URI = 'mongodb://localhost:27017/'
MONGO_DATABASE = 'test'
OPLOG_SETTINGS = {
    'roll_time': 2,
    'ns': 'test.testtable'  # 监听指定coll内的doc变化
    # 'ns': 'test' # 监听指定coll的变化
}

PIKA_PARAMS = {
    'host': 'localhost',  # amqp.server.com
    'username': 'test',  # convenience param for username
    'password': '123',  # convenience param for password
    'port': 5672,  # amqp server port
    'virtual_host': '/'  # amqp vhost
}

MQ_BIND_RELATION = {
    # exchange_type:{queue_name:[exchange_names,]}
    'fanout': {'quota': ['huobi', 'okex']}
}

