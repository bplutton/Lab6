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

def test_parse_availability_when_in_stock(valid_product):
    # Arrange

    # Act
    availability = parse_availability(valid_product)

    # Assert
    assert availability is True

def test_parse_availability_when_out_of_stock(product_out_of_stock):
    # Arrange

    # Act
    availability = parse_availability(product_out_of_stock)

    # Assert
    assert availability is False

def test_parse_availability_when_field_missing(minimal_product):
    # Arrange

    # Act
    availability = parse_availability(minimal_product)

    # Assert
    assert availability is False