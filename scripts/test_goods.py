import pytest
from fixtures.goods import goods_list
from loguru import logger


def setup_module():
    print("setup_module执行")


class TestGoods:

    # def setup_class(self):
    #     print("setup_class执行")

    # def setup_method(self):
    #     print("setup_method执行")

    @pytest.mark.usefixtures(goods_list.__name__)
    @pytest.mark.skip("token失效跳过")
    def test_goods_list(self, session):
        res = session.post(
            "goods/list",
            json={
                "page": 1,
                "size": 5
            }
        )

        assert res.status_code == 200
        assert res.json()["code"] == 0, res.text

    def test_demo_1(self):
        logger.info("test_demo_1测试")

    def test_demo_2(self):
        logger.info("test_demo_2测试")
