import math
cart_value: int
delivery_distance: int
number_of_items: int
time: str
delivery_fee: int

cart_value_fee: int
delivery_distance_fee: int
number_of_items_fee: int
time_fee: float


delivery_fee: int = (cart_value_fee + delivery_distance_fee + number_of_items_fee)* time_fee

def get_cart_value_fee(cart_value: int) -> int:
   min_value = 1000
   surcharge: int = min_value - cart_value
   if surcharge > 0:
      return surcharge
   else: return 0

    
def get_delivery_distance_fee(delivery_distance: int) -> int:
    min_fee = 100
    base_fee = 200
    add_fee = 100
    if delivery_distance < 500:
       return min_fee
    else:
        segments: float = (delivery_distance-1000)/500
        rounded_segments: int = math.ceil(segments)
        return base_fee + rounded_segments*add_fee

def get_number_of_items_fee(number_of_items: int) -> int:
    min_number = 5 
    max_number = 12
    number_fee = 50
    extra_fee = 120

    if  number_of_items - max_number > 0 :
        return (number_of_items - max_number) * number_fee + extra_fee
 
    if  number_of_items - min_number > 0 :
        return (number_of_items - max_number) * number_fee
    
    else: return 0 
    
def get_time_fee(time: str) -> float:
    time_index: float = 1.2
    if time== 'friday':
        return time_index
    else: return 1

def get_delivery_fee(cart_value: int, delivery_distance: int, number_of_items: int, time: str):
    free_delivery = 20000
    max_delivery_fee = 1500
    if cart_value >= free_delivery:
        return 0
    cart_value_fee: int = get_cart_value_fee(cart_value)
    delivery_distance_fee: int = get_delivery_distance_fee(delivery_distance)
    number_of_items_fee: int = get_number_of_items_fee(number_of_items)
    time_fee: float = get_time_fee(time)
    delivery_fee: int = (cart_value_fee + delivery_distance_fee + number_of_items_fee) * time_fee 
    if delivery_fee > max_delivery_fee: 
        return max_delivery_fee
    else: delivery_fee 