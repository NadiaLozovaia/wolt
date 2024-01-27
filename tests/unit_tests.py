import pytest
from app.fee_calculator import (
    get_cart_value_fee,
    get_delivery_distance_fee,
    get_number_items_fee,
    get_time_fee,
    get_delivery_fee,
)
from datetime import datetime


def test_get_cart_value_fee():
    assert get_cart_value_fee(890) == 110
    assert get_cart_value_fee(1000) == 0
    assert get_cart_value_fee(999) == 1
    assert get_cart_value_fee(10001) == 0
    with pytest.raises(ValueError):
        get_cart_value_fee(-1)


def test_get_delivery_distance_fee():
    assert get_delivery_distance_fee(499) == 100
    assert get_delivery_distance_fee(500) == 200
    assert get_delivery_distance_fee(501) == 200
    assert get_delivery_distance_fee(1000) == 200
    assert get_delivery_distance_fee(1499) == 300
    assert get_delivery_distance_fee(1500) == 300
    assert get_delivery_distance_fee(1501) == 400
    assert get_delivery_distance_fee(0) == 100
    with pytest.raises(ValueError):
        get_delivery_distance_fee(-1)


def test_get_number_items_fee():
    assert get_number_items_fee(4) == 0
    assert get_number_items_fee(5) == 50
    assert get_number_items_fee(10) == 300
    assert get_number_items_fee(12) == 400
    assert get_number_items_fee(13) == 570
    assert get_number_items_fee(14) == 620
    with pytest.raises(ValueError):
        get_number_items_fee(-1)


def test_get_time_fee():
    assert get_time_fee(datetime.fromisoformat("2024-01-15T13:00:00Z")) == 1
    assert get_time_fee(datetime.fromisoformat("2024-01-15T15:00:00Z")) == 1
    assert get_time_fee(datetime.fromisoformat("2024-01-15T15:00:01Z")) == 1
    assert get_time_fee(datetime.fromisoformat("2024-01-15T18:59:00Z")) == 1
    assert get_time_fee(datetime.fromisoformat("2024-01-15T19:00:00Z")) == 1
    assert get_time_fee(datetime.fromisoformat("2024-01-19T13:00:00Z")) == 1
    assert get_time_fee(datetime.fromisoformat("2024-01-19T15:00:00Z")) == 1.2
    assert get_time_fee(datetime.fromisoformat("2024-01-19T15:00:01Z")) == 1.2
    assert get_time_fee(datetime.fromisoformat("2024-01-19T18:59:59Z")) == 1.2
    assert get_time_fee(datetime.fromisoformat("2024-01-19T19:00:00Z")) == 1


def test_get_delivery_fee():
    assert (
        get_delivery_fee(790, 2235, 4, datetime.fromisoformat("2024-01-15T13:00:00Z"))
        == 710
    )
    assert (
        get_delivery_fee(790, 2235, 4, datetime.fromisoformat("2024-01-19T15:00:00Z"))
        == 852
    )
    assert (
        get_delivery_fee(1000, 2235, 4, datetime.fromisoformat("2024-01-19T15:00:00Z"))
        == 600
    )
    assert (
        get_delivery_fee(1000, 2235, 4, datetime.fromisoformat("2024-01-19T13:00:00Z"))
        == 500
    )
    assert (
        get_delivery_fee(
            200000, 2235, 4, datetime.fromisoformat("2024-01-15T13:00:00Z")
        )
        == 0
    )
    assert (
        get_delivery_fee(
            200000, 2235, 120, datetime.fromisoformat("2024-01-19T15:00:00Z")
        )
        == 0
    )
    assert (
        get_delivery_fee(
            1000, 223500, 4, datetime.fromisoformat("2024-01-19T13:00:00Z")
        )
        == 1500
    )
    assert (
        get_delivery_fee(1000, 499, 200, datetime.fromisoformat("2024-01-19T13:00:00Z"))
        == 1500
    )
    assert (
        get_delivery_fee(0, 499, 200, datetime.fromisoformat("2024-01-19T13:00:00Z"))
        == 1500
    )
