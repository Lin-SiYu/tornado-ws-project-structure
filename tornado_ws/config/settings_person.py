MONGO_URI = 'mongodb://localhost:27017/'
MONGO_DATABASE = 'test'
OPLOG_SETTINGS = {
    'roll_time': 2,
    'ns': 'test.testtable'  # 监听指定coll内的doc变化
    # 'ns': 'test' # 监听指定coll的变化
}
