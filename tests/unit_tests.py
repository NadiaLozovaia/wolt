import pytest
from app.fee_calculator import (
    get_cart_value_fee,
    get_delivery_distance_fee,
    get_items_number_fee,
    get_rush_hour_multiplier,
    get_delivery_fee,
)
from datetime import datetime


def test_get_cart_value_fee():
    assert get_cart_value_fee(890) == 110
    assert get_cart_value_fee(1000) == 0
    assert get_cart_value_fee(999) == 1
    assert get_cart_value_fee(10001) == 0



def test_get_delivery_distance_fee():
    assert get_delivery_distance_fee(0) == 200
    assert get_delivery_distance_fee(1) == 200
    assert get_delivery_distance_fee(999) == 200
    assert get_delivery_distance_fee(1000) == 200
    assert get_delivery_distance_fee(1001) == 300
    assert get_delivery_distance_fee(1499) == 300
    assert get_delivery_distance_fee(1500) == 300
    assert get_delivery_distance_fee(1501) == 400



def test_get_number_items_fee():
    assert get_items_number_fee(4) == 0
    assert get_items_number_fee(5) == 50
    assert get_items_number_fee(10) == 300
    assert get_items_number_fee(12) == 400
    assert get_items_number_fee(13) == 570
    assert get_items_number_fee(14) == 620
 


def test_get_rush_hour_multiplier():
    assert get_rush_hour_multiplier(datetime.fromisoformat("2024-01-15T13:00:00Z")) == 1
    assert get_rush_hour_multiplier(datetime.fromisoformat("2024-01-15T15:00:00Z")) == 1
    assert get_rush_hour_multiplier(datetime.fromisoformat("2024-01-15T15:00:01Z")) == 1
    assert get_rush_hour_multiplier(datetime.fromisoformat("2024-01-15T18:59:00Z")) == 1
    assert get_rush_hour_multiplier(datetime.fromisoformat("2024-01-15T19:00:00Z")) == 1
    assert get_rush_hour_multiplier(datetime.fromisoformat("2024-01-19T13:00:00Z")) == 1
    assert get_rush_hour_multiplier(datetime.fromisoformat("2024-01-19T15:00:00Z")) == 1.2   
    assert get_rush_hour_multiplier(datetime.fromisoformat("2024-01-19T15:00:01Z")) == 1.2
    assert get_rush_hour_multiplier(datetime.fromisoformat("2024-01-19T18:59:59Z")) == 1.2
    assert get_rush_hour_multiplier(datetime.fromisoformat("2024-01-19T19:00:00Z")) == 1


def test_get_delivery_fee():
    assert get_delivery_fee(790, 2235, 4, datetime.fromisoformat("2024-01-15T13:00:00Z")) == 710   
    assert get_delivery_fee(790, 2235, 4, datetime.fromisoformat("2024-01-19T15:00:00Z")) == 852  
    assert get_delivery_fee(1000, 2235, 4, datetime.fromisoformat("2024-01-19T15:00:00Z")) == 600
    assert get_delivery_fee(1000, 2235, 4, datetime.fromisoformat("2024-01-19T13:00:00Z")) == 500
    assert get_delivery_fee(1000, 1000, 4, datetime.fromisoformat("2024-01-19T13:00:00Z")) == 200
    assert get_delivery_fee(1000, 1001, 4, datetime.fromisoformat("2024-01-19T13:00:00Z")) == 300
    assert get_delivery_fee(200000, 2235, 4, datetime.fromisoformat("2024-01-15T13:00:00Z")) == 0
    assert get_delivery_fee(200000, 2235, 120, datetime.fromisoformat("2024-01-19T15:00:00Z")) == 0
    assert get_delivery_fee(1000, 223500, 4, datetime.fromisoformat("2024-01-19T13:00:00Z")) == 1500
    assert get_delivery_fee(1000, 499, 200, datetime.fromisoformat("2024-01-19T13:00:00Z")) == 1500
    assert get_delivery_fee(0, 499, 200, datetime.fromisoformat("2024-01-19T13:00:00Z")) == 1500

