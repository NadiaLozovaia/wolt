import math
from datetime import datetime
from app import config

EUR = 100


def get_cart_value_fee(cart_value: int) -> int:
    """
    Calculates the surcharge depending on amount of cart value.

    Args:
        cart_value (int): Cart value in cents.

    Returns:
        int: The surcharge in cents.

    """

    surcharge = config.min_value - cart_value
    return max(surcharge, 0)


def get_delivery_distance_fee(delivery_distance: int) -> int:
    """
    Calculates the fee depending on the distance.

    Args:
        delivery_distance (int): Distance in meters.

    Returns:
        int: The fee in cents.

    """
    if delivery_distance <= config.base_distance:
        return config.base_fee
    segments = (delivery_distance - config.base_distance) / config.segment_size
    rounded_segments = math.ceil(segments)
    return config.base_fee + rounded_segments * config.add_fee


def get_items_number_fee(
    number_of_items: int,
) -> int:
    """
    Calculates the surcharge depending on number of items in a cart.

    Args:
        number_of_items (int): Number of items.

    Returns:
        int: The surcharge in cents.

    """

    if number_of_items > config.max_number:
        return (number_of_items - config.min_number) * config.number_fee + config.extra_bulk_fee
    if number_of_items > config.min_number:
        return (number_of_items - config.min_number) * config.number_fee
    return 0


def get_rush_hour_multiplier(
    delivery_date: datetime,
) -> float:
    """
    Calculates the multiplier of rush hour depending on day of the week and time.

    Args:
        delivery_date (datetime): Order time in UTC in ISO format.

    Returns:
        float: Multiplier factor.

    """
    weekday = delivery_date.weekday()
    current_hour = delivery_date.hour
    if weekday == config.rush_week_day and config.rush_start_hour <= current_hour < config.rush_end_hour:
        return config.rush_index
    return 1


def get_delivery_fee(
    cart_value: int,
    delivery_distance: int,
    number_of_items: int,
    delivery_date: datetime,
) -> int:
    """
    Calculates the delivery fee for a cart.
    The function rounds the delivery_fee up to integers.
    Args:
        cart_value (int): Cart value in cents.
        delivery_distance (int): Distance in meters.
        number_of_items (int): Number of items in the cart.
        delivery_date (datetime): Date and time of delivery.
    Returns:
        int: The delivery fee in cents.

    """

    if cart_value >= config.free_delivery:
        return 0
    cart_value_fee: int = get_cart_value_fee(cart_value)
    delivery_distance_fee: int = get_delivery_distance_fee(delivery_distance)
    number_of_items_fee: int = get_items_number_fee(number_of_items)
    time_fee: float = get_rush_hour_multiplier(delivery_date)
    delivery_fee = (
        cart_value_fee + delivery_distance_fee + number_of_items_fee
    ) * time_fee
    delivery_fee = math.ceil(delivery_fee)
    return min(delivery_fee, config.max_delivery_fee)
