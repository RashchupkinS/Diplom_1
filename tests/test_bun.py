import pytest
from praktikum.bun import Bun
from data import buns_name_price




class TestBun:

    @pytest.mark.parametrize("bun_name, bun_price", buns_name_price)
    def test_get_name_return_name(self, bun_name, bun_price):
        bun = Bun(name=bun_name, price=bun_price)
        assert bun.get_name() == bun_name


    @pytest.mark.parametrize("bun_name, bun_price", buns_name_price)
    def test_get_price_return_price(self, bun_name, bun_price):
        bun = Bun(name=bun_name, price=bun_price)
        assert bun.get_price() == bun_price




