import pytest
from parser import parse_product_basic, parse_availability

def test_parse_product_basic_extracts_id(valid_product):
    # Arrange

    # Act
    response = parse_product_basic(valid_product)

    # Assert
    assert response["id"] == "prod_12345"

def test_parse_product_basic_extracts_name(valid_product):
    # Arrange

    # Act
    response = parse_product_basic(valid_product)

    # Assert
    assert response["name"] == "Wireless Bluetooth Headphones"

def test_parse_product_basic_returns_only_id_and_name(valid_product):
    # Arrange

    # Act
    response = parse_product_basic(valid_product)

    # Assert
    assert set(response.keys()) == {"id", "name"}