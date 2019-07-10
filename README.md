# tornado-ws-project-structure
A tornado project that contains components

# 一、Middleware 组件

[详细信息请参考博客](https://blog.csdn.net/qq_33961117/article/details/95335533)

添加了 Middleware 组件基类，位于 common_utilties 目录下

```python
# 使用中间件的 ws 类必须继承 WSMiddle
class TestWebSocketHandler(WSMiddle):
    # 若自定义 middleware_list ，则不使用配置文件内信息
    # middleware_list = []
    def msg_handle(self, message):
        print(message)
```

## 1-1 ping-pong middleware

基于 Middleware 添加了 业务逻辑上的 ping-pong 处理，ws 建立连接后，每 5s 发送 经过 gzip 压缩的数据给client - {‘ping’:13位时间戳}，client 必须返回同格式，同 pong 数据给 server 端 - {‘pong’:13位时间戳}

若 server 连续俩次未接收到返回，则自动断开连接。

如下位置配置:

```python
MIDDLEWARE_LIST = ['tornado_ws.common_utilities.middleware.pingmiddle.PingMiddleware']
```



