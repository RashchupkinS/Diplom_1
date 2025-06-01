import pytest
import allure
from unittest.mock import Mock
from praktikum.database import Database
from praktikum.burger import Burger




@pytest.fixture
def database():
    with allure.step("Создать экземпляр базы данных"):
        return Database()


@pytest.fixture
def mock_bun():
    with allure.step("Создать экземпляр mock-булки"):
        return Mock()


@pytest.fixture
def mock_ingredient_1():
    with allure.step("Создать экземпляр mock-ингредиента"):
        return Mock()


@pytest.fixture
def mock_ingredient_2():
    with allure.step("Создать экземпляр mock-ингредиента"):
        return Mock()


@pytest.fixture
def burger():
    with allure.step("Создать экземпляр бургера"):
        return Burger()




