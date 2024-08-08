import pytest
from utils.http import Http
import os
from dotenv import load_dotenv
from utils import log


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="dev", help="environment：dev, prod"
    )


def pytest_configure(config):
    # 设置环境
    env = config.getoption("env")
    e = f".env.{env}"
    if not os.path.exists(e):
        raise ValueError(f"env模式：{env}，不存在")

    load_dotenv(dotenv_path=e)

    # 初始化日志
    log.register()


# 创建全局session
@pytest.fixture(scope="session", autouse=True)
def session():
    base_url = os.getenv("BASE_URL")
    headers = {"Authorization": os.getenv("TOKEN")}

    session = Http(
        base_url=base_url,
        default_headers=headers,
    ).create()

    # 添加响应钩子(公共断言)
    # session.hooks.update(dict(response=assert_status_code))

    yield session

    session.close()


def assert_status_code(response, *args, **kwargs):
    assert response.status_code == 200, f"请求状态码错误：{response.status_code} != 200"
