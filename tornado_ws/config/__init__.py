from tornado_ws.config import settings_default, settings_person


class Settings():
    def __init__(self):
        # 集成全局默认配置
        self.__setAttr(settings_default)

        # 自定义配置(覆盖相同默认配置)
        self.__setAttr(settings_person)

    def __setAttr(self, conf):
        for key in dir(conf):
            if key.isupper():
                v = getattr(conf, key)
                setattr(self, key, v)


setting = Settings()
