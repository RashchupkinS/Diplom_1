import pytest
import allure
from data import expected_buns, expected_ingredients




class TestDatabase:

    @allure.title("Проверка, что метод available_ingredients возвращает список")
    def test_available_buns_returns_list(self, database):
        with allure.step("Проверяем, что результат available_buns является списком"):
            assert isinstance(database.available_buns(), list)


    @pytest.mark.parametrize("index, bun_name, bun_price", expected_buns)
    @allure.title("Проверка базы данных на наличие имени булки")
    def test_available_buns_contains_expected_bun(self, database, index, bun_name, bun_price):
        buns = database.available_buns()
        assert buns[index].name == bun_name


    @pytest.mark.parametrize("index, bun_name, bun_price", expected_buns)
    @allure.title("Проверка базы данных на наличие цены булки")
    def test_available_buns_contains_expected_price(self, database, index, bun_name, bun_price):
        buns = database.available_buns()
        assert buns[index].price == bun_price


    @allure.title("Проверка, что метод available_ingredients возвращает список")
    def test_available_ingredients_returns_list(self, database):
        with allure.step("Проверяем, что результат available_ingredients является списком"):
            assert isinstance(database.available_ingredients(), list)


    @pytest.mark.parametrize("index, ingredient_type, ingredient_name, ingredient_price", expected_ingredients)
    @allure.title("Проверка базы данных на наличие типа ингредиента")
    def test_available_ingredients_type_contains_expected_type(
            self, database, index, ingredient_type, ingredient_name, ingredient_price):
        ingredients = database.available_ingredients()
        assert ingredients[index].type == ingredient_type


    @pytest.mark.parametrize("index, ingredient_type, ingredient_name, ingredient_price", expected_ingredients)
    @allure.title("Проверка базы данных на наличие имени ингредиента")
    def test_available_ingredients_type_contains_expected_name(
            self, database, index, ingredient_type, ingredient_name, ingredient_price):
        ingredients = database.available_ingredients()
        assert ingredients[index].name == ingredient_name


    @pytest.mark.parametrize("index, ingredient_type, ingredient_name, ingredient_price", expected_ingredients)
    @allure.title("Проверка базы данных на наличие цены ингредиента")
    def test_available_ingredients_type_contains_expected_price(
            self, database, index, ingredient_type, ingredient_name, ingredient_price):
        ingredients = database.available_ingredients()
        assert ingredients[index].price == ingredient_price




