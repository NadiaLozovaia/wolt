import math
from datetime import datetime

EUR = 100


def get_cart_value_fee(cart_value: int) -> int:
    if cart_value < 0:
        raise ValueError("cart value can not be negative")
    min_value = 10 * EUR
    surcharge = min_value - cart_value
    return max(surcharge, 0)


def get_delivery_distance_fee(delivery_distance: int) -> int:
    base_fee = 2 * EUR
    base_distance = 1000
    segment_size = 500
    add_fee = 1 * EUR
    if delivery_distance < 0:
        raise ValueError("delivery distance can not be negative")
    if delivery_distance <= base_distance:
        return base_fee
    segments = (delivery_distance - base_distance) / segment_size
    rounded_segments = math.ceil(segments)
    return base_fee + rounded_segments * add_fee


def get_items_number_fee(
    number_of_items: int,
) -> int:
    min_number = 4
    max_number = 12
    number_fee = 0.5 * EUR
    extra_bulk_fee = 1.2 * EUR
    if number_of_items < 0:
        raise ValueError("number of items can not be negative")
    if number_of_items > max_number:
        return (number_of_items - min_number) * number_fee + extra_bulk_fee
    if number_of_items > min_number:
        return (number_of_items - min_number) * number_fee
    return 0


def get_rush_hour_multiplier(
    delivery_date: datetime,
) -> float:
    weekday = delivery_date.weekday()
    current_hour = delivery_date.hour
    if weekday == 4 and 15 <= current_hour < 19:
        return 1.2
    return 1


def get_delivery_fee(
    cart_value: int,
    delivery_distance: int,
    number_of_items: int,
    delivery_date: datetime,
) -> int:
    free_delivery = 20000
    max_delivery_fee = 1500

    if cart_value >= free_delivery:
        return 0
    cart_value_fee: int = get_cart_value_fee(cart_value)
    delivery_distance_fee: int = get_delivery_distance_fee(delivery_distance)
    number_of_items_fee: int = get_items_number_fee(number_of_items)
    time_fee: float = get_rush_hour_multiplier(delivery_date)
    delivery_fee = (
        cart_value_fee + delivery_distance_fee + number_of_items_fee
    ) * time_fee
    delivery_fee = math.ceil(delivery_fee) 
    if delivery_fee > max_delivery_fee:
        return max_delivery_fee

    return delivery_fee



