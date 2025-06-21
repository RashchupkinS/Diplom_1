import pytest
from unittest.mock import Mock
from data import buns_name_price, ingredients_type_name_price
from praktikum.burger import Burger




class TestBurger:

    @pytest.mark.parametrize("bun_name, bun_price", buns_name_price)
    def test_set_buns_set_burgers_bun(self, bun_name, bun_price):
        mock_bun = Mock()
        mock_bun.name = bun_name
        mock_bun.price = bun_price
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun.name == bun_name, f"Ожидаемая булка: {bun_name}, получена булка: {burger.bun.name}"
        assert burger.bun.price == bun_price, f"Ожидаемая цена: {bun_price}, получена цена: {burger.bun.price}"


    def test_add_ingredient_add_object_to_list(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]


    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price", ingredients_type_name_price)
    def test_add_ingredient_add_object_with_attributes_type_name_price(
            self, ingredient_type, ingredient_name, ingredient_price):
        mock_ingredient = Mock()
        mock_ingredient.type = ingredient_type
        mock_ingredient.name = ingredient_name
        mock_ingredient.price = ingredient_price
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0].type == ingredient_type, (f"Ожидаемый тип: {ingredient_type}, "
                                                                   f"получен тип: {burger.ingredients[0].type}")
        assert burger.ingredients[0].name == ingredient_name, (f"Ожидаемый ингредиент: {ingredient_name}, "
                                                                   f"получен ингредиент: {burger.ingredients[0].name}")
        assert burger.ingredients[0].price == ingredient_price, (f"Ожидаемая цена: {ingredient_price}, "
                                                                     f"получена цена: {burger.ingredients[0].price}")


    def test_remove_ingredient_add_two_ingredients_and_remove_one_by_index(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.ingredients = [mock_ingredient, mock_ingredient]
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1


    def test_move_ingredient_add_two_ingredients_and_swap_them_by_index(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger.ingredients.append(mock_ingredient_1)
        burger.ingredients.append(mock_ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ingredient_2, mock_ingredient_1]


    def test_get_price_return_burger_price(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 988.0
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        mock_ingredient_1.get_price.return_value = 90.0
        mock_ingredient_2.get_price.return_value = 424.0
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients.append(mock_ingredient_1)
        burger.ingredients.append(mock_ingredient_2)
        assert burger.get_price() == 2490.0  #  988.0*2 + 90.0 + 424.0


    def test_get_receipt_return_burger_receipt(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = buns_name_price[0][0]
        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_type.return_value = ingredients_type_name_price[0][0].lower()
        mock_ingredient_1.get_name.return_value = ingredients_type_name_price[0][1]
        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_type.return_value = ingredients_type_name_price[-1][0].lower()
        mock_ingredient_2.get_name.return_value = ingredients_type_name_price[-1][1]
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients.append(mock_ingredient_1)
        burger.ingredients.append(mock_ingredient_2)
        burger.get_price = Mock(return_value=2490.0)
        receipt = burger.get_receipt()
        expected_receipt = (
            f"(==== {buns_name_price[0][0]} ====)\n"
            f"= {ingredients_type_name_price[0][0].lower()} {ingredients_type_name_price[0][1]} =\n"
            f"= {ingredients_type_name_price[-1][0].lower()} {ingredients_type_name_price[-1][1]} =\n"
            f"(==== {buns_name_price[0][0]} ====)\n"
            f"\n"
            f"Price: {burger.get_price.return_value}"
        )
        assert receipt == expected_receipt


