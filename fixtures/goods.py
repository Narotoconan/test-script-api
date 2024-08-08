import pytest


@pytest.fixture(scope='function')
def goods_list(session):
    yield
    print("goods列表后置操作")
