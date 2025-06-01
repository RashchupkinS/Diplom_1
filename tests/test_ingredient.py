import pytest
import allure
from praktikum.ingredient import Ingredient
from data import ingredients_type_name_price




class TestIngredient:

    @allure.title("Проверка корректного возврата цены ингредиента методом get_price, класса Ingredients")
    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price", ingredients_type_name_price)
    def test_get_price_add_ingredient_and_check_price(self, ingredient_type, ingredient_name, ingredient_price):
        with allure.step(f"Создаем ингредиент: тип = {ingredient_type}, имя = {ingredient_name}, цена = {ingredient_price}"):
            ingredient = Ingredient(ingredient_type=ingredient_type, name=ingredient_name, price=ingredient_price)
        with allure.step("Проверяем, что метод get_price возвращает правильную цену"):
            assert ingredient.get_price() == ingredient_price


    @allure.title("Проверка корректного возврата названия ингредиента методом get_name, класса Ingredients")
    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price", ingredients_type_name_price)
    def test_get_name_add_ingredient_and_check_name(self, ingredient_type, ingredient_name, ingredient_price):
        with allure.step(f"Создаем ингредиент с именем '{ingredient_name}'"):
            ingredient = Ingredient(ingredient_type=ingredient_type, name=ingredient_name, price=ingredient_price)
        with allure.step("Проверяем, что метод get_name возвращает правильное имя"):
            assert ingredient.get_name() == ingredient_name


    @allure.title("Проверка корректного возврата типа ингредиента методом get_type, класса Ingredients")
    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price", ingredients_type_name_price)
    def test_get_type_add_ingredient_and_check_type(self, ingredient_type, ingredient_name, ingredient_price):
        with allure.step(f"Создаем ингредиент типа '{ingredient_type}'"):
            ingredient = Ingredient(ingredient_type=ingredient_type, name=ingredient_name, price=ingredient_price)
        with allure.step("Проверяем, что метод get_type возвращает правильный тип"):
            assert ingredient.get_type() == ingredient_type




