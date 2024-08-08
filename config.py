import os
from functools import lru_cache


class Config:

    def __init__(self):
        # 设置项目根目录
        self.ROOT_PATH = os.path.abspath(__file__).split(os.path.relpath(__file__))[0]

        # 日志配置项
        self.LOG_LEVEL: str = os.getenv("LOG_LEVEL") or "INFO"
        self.LOG_PATH: str = self.ROOT_PATH + "logs/{time:YYYY-MM-DD}.log"
        self.LOG_RETENTION: str = os.getenv("LOG_RETENTION") or "14 days"


@lru_cache()
def get_config():
    return Config()
