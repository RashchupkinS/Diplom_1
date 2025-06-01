import pytest
import allure
from praktikum.bun import Bun
from data import buns_name_price




class TestBun:

    @allure.title("Проверка корректного возврата названия булки '{bun_name}' методом get_name, класса Bun")
    @pytest.mark.parametrize("bun_name, bun_price", buns_name_price)
    def test_get_name(self, bun_name, bun_price):
        with allure.step(f"Создаем булку с именем '{bun_name}' и ценой {bun_price}"):
            bun = Bun(name=bun_name, price=bun_price)
        with allure.step("Проверяем, что метод get_name возвращает корректное имя булки"):
            assert bun.get_name() == bun_name


    @allure.title("Проверка корректного возврата цены булки '{bun_price}' методом get_price, класса Bun")
    @pytest.mark.parametrize("bun_name, bun_price", buns_name_price)
    def test_get_price(self, bun_name, bun_price):
        with allure.step(f"Создаем булку с именем '{bun_name}' и ценой {bun_price}"):
            bun = Bun(name=bun_name, price=bun_price)
        with allure.step("Проверяем, что метод get_price возвращает корректную цену булки"):
            assert bun.get_price() == bun_price




