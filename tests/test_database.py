import pytest
from data import expected_buns, expected_ingredients




class TestDatabase:

    def test_available_buns_returns_list(self, database):
        assert isinstance(database.available_buns(), list)


    @pytest.mark.parametrize("index, bun_name, bun_price", expected_buns)
    def test_available_buns_contains_expected_bun(self, database, index, bun_name, bun_price):
        buns = database.available_buns()
        assert buns[index].name == bun_name


    @pytest.mark.parametrize("index, bun_name, bun_price", expected_buns)
    def test_available_buns_contains_expected_price(self, database, index, bun_name, bun_price):
        buns = database.available_buns()
        assert buns[index].price == bun_price


    def test_available_ingredients_returns_list(self, database):
        assert isinstance(database.available_ingredients(), list)


    @pytest.mark.parametrize("index, ingredient_type, ingredient_name, ingredient_price", expected_ingredients)
    def test_available_ingredients_type_contains_expected_type(
            self, database, index, ingredient_type, ingredient_name, ingredient_price):
        ingredients = database.available_ingredients()
        assert ingredients[index].type == ingredient_type


    @pytest.mark.parametrize("index, ingredient_type, ingredient_name, ingredient_price", expected_ingredients)
    def test_available_ingredients_type_contains_expected_name(
            self, database, index, ingredient_type, ingredient_name, ingredient_price):
        ingredients = database.available_ingredients()
        assert ingredients[index].name == ingredient_name


    @pytest.mark.parametrize("index, ingredient_type, ingredient_name, ingredient_price", expected_ingredients)
    def test_available_ingredients_type_contains_expected_price(
            self, database, index, ingredient_type, ingredient_name, ingredient_price):
        ingredients = database.available_ingredients()
        assert ingredients[index].price == ingredient_price




