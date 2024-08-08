import sys
from loguru import logger
from config import get_config


def register():
    _config = get_config()

    level = _config.LOG_LEVEL
    path = _config.LOG_PATH
    retention = _config.LOG_RETENTION

    # 清除
    logger.remove()
    # 添加日志处理器
    # logger.add(sys.stdout, level=level)
    logger.add(path, retention=retention, rotation="00:00", level=level, encoding="utf8")
