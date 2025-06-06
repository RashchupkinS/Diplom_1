import pytest
from unittest.mock import Mock
from praktikum.database import Database
from praktikum.burger import Burger


# фикстура создает экземпляр класса Database
@pytest.fixture
def database():
    return Database()

# фикстура создает экземпляр mock-булки
@pytest.fixture
def mock_bun():
    return Mock()

# фикстура создает экземпляр mock-ингредиента
@pytest.fixture
def mock_ingredient_1():
    return Mock()

# фикстура создает экземпляр mock-ингредиента
@pytest.fixture
def mock_ingredient_2():
    return Mock()

# фикстура создает экземпляр бургера
@pytest.fixture
def burger():
    return Burger()