import pytest
import allure
from unittest.mock import Mock
from data import buns_name_price, ingredients_type_name_price




class TestBurger:

    @allure.title("Проверка установки булки в бургер")
    @pytest.mark.parametrize("bun_name, bun_price", buns_name_price)
    def test_set_buns(self, mock_bun, burger, bun_name, bun_price):
        with allure.step("Установка атрибутов mock-булки"):
            mock_bun.name = bun_name
            mock_bun.price = bun_price
        with allure.step("Установка булки в бургер"):
            burger.set_buns(mock_bun)
        with allure.step("Проверка имени и цены булки"):
            assert burger.bun.name == bun_name, f"Ожидаемая булка: {bun_name}, получена булка: {burger.bun.name}"
            assert burger.bun.price == bun_price, f"Ожидаемая цена: {bun_price}, получена цена: {burger.bun.price}"


    @allure.title("Проверка добавления одного экземпляра ингредиента в список ингредиентов")
    def test_add_ingredient_add_object_to_list(self, mock_ingredient_1, burger):
        with allure.step("Добавление ингредиента методом add_ingredient"):
            burger.add_ingredient(mock_ingredient_1)
        with allure.step("Проверка содержания экземпляра ингредиента в списке ингредиентов"):
            assert burger.ingredients == [mock_ingredient_1]


    @allure.title("Проверка добавления ингредиента на наличие атрибутов type, name, price")
    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price", ingredients_type_name_price)
    def test_add_ingredient_add_object_with_attributes_type_name_price(
            self, mock_ingredient_1, burger, ingredient_type, ingredient_name, ingredient_price):
        with allure.step("Установка атрибутов mock-ингредиента"):
            mock_ingredient_1.type = ingredient_type
            mock_ingredient_1.name = ingredient_name
            mock_ingredient_1.price = ingredient_price
        with allure.step("Добавление ингредиента в бургер"):
            burger.add_ingredient(mock_ingredient_1)
        with allure.step("Проверка наличия атрибутов у ингредиента"):
            assert burger.ingredients[0].type == ingredient_type, (f"Ожидаемый тип: {ingredient_type}, "
                                                                   f"получен тип: {burger.ingredients[0].type}")
            assert burger.ingredients[0].name == ingredient_name, (f"Ожидаемый ингредиент: {ingredient_name}, "
                                                                   f"получен ингредиент: {burger.ingredients[0].name}")
            assert burger.ingredients[0].price == ingredient_price, (f"Ожидаемая цена: {ingredient_price}, "
                                                                     f"получена цена: {burger.ingredients[0].price}")


    @allure.title("Проверка удаления ингредиента по индексу")
    def test_remove_ingredient_add_two_ingredients_and_remove_one_by_index(self, mock_ingredient_1, burger):
        with allure.step("Добавление двух одинаковых ингредиентов"):
            burger.ingredients = [mock_ingredient_1, mock_ingredient_1]
        with allure.step("Удаление ингредиента по индексу"):
            burger.remove_ingredient(0)
        with allure.step("Проверка количества оставшихся ингредиентов"):
            assert len(burger.ingredients) == 1


    @allure.title("Проверка перемещения ингредиентов по индексам")
    def test_move_ingredient_add_two_ingredients_and_swap_them_by_index(
            self, mock_ingredient_1, mock_ingredient_2, burger):
        with allure.step("Создание двух ингредиентов и добавление их в бургер"):
            burger.ingredients.append(mock_ingredient_1)
            burger.ingredients.append(mock_ingredient_2)
        with allure.step("Перемещение ингредиентов методом move_ingredient"):
            burger.move_ingredient(0, 1)
        with allure.step("Проверка порядка перемещенных ингредиентов"):
            assert burger.ingredients == [mock_ingredient_2, mock_ingredient_1]


    @allure.title("Проверка расчета итоговой цены бургера")
    def test_get_price(self, mock_bun, mock_ingredient_1, mock_ingredient_2, burger):
        with allure.step("Создание цен для ингредиентов, через return_value"):
            mock_bun.get_price.return_value = 988.0
            mock_ingredient_1.get_price.return_value = 90.0
            mock_ingredient_2.get_price.return_value = 424.0
            burger.bun = mock_bun
            burger.ingredients.append(mock_ingredient_1)
            burger.ingredients.append(mock_ingredient_2)
        with allure.step("Проверка итоговой цены методом get_price"):
            assert burger.get_price() == 2490.0  # 988.0*2 + 90.0 + 424.0


    @allure.title("Проверка расположения элементов в чеке бургера")
    def test_get_receipt(self, mock_bun, mock_ingredient_1, mock_ingredient_2, burger):
        with allure.step("Установка булки и ингредиентов для бургера"):
            mock_bun.get_name.return_value = buns_name_price[0][0]
            mock_ingredient_1.get_type.return_value = ingredients_type_name_price[0][0].lower()
            mock_ingredient_1.get_name.return_value = ingredients_type_name_price[0][1]
            mock_ingredient_2.get_type.return_value = ingredients_type_name_price[-1][0].lower()
            mock_ingredient_2.get_name.return_value = ingredients_type_name_price[-1][1]
        with allure.step("Добавление булки и ингредиентов в бургер"):
            burger.bun = mock_bun
            burger.ingredients.append(mock_ingredient_1)
            burger.ingredients.append(mock_ingredient_2)
            burger.get_price = Mock(return_value=2490.0)
        with allure.step("Формирование чека методом get_receipt"):
            receipt = burger.get_receipt()
        with allure.step("Проверка строк в чеке"):
            expected_lines = [
                f"(==== {buns_name_price[0][0]} ====)",
                f"= {ingredients_type_name_price[0][0].lower()} {ingredients_type_name_price[0][1]} =",
                f"= {ingredients_type_name_price[-1][0].lower()} {ingredients_type_name_price[-1][1]} =",
                f"(==== {buns_name_price[0][0]} ====)",
                f"Price: {burger.get_price.return_value}"
            ]
        for line in expected_lines:
            assert line in receipt




