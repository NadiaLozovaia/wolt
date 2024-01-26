# General comments:
# 1. code format
# 2. Remove unused variables
# 3. Everywhere where you use values in cents it is better to write something like 20 * 100 (20 euros) instead of 20000.
# Maybe it is even better to create a global variable called 
# EUR = 100
# And everywhere where you have some values make it like
# asd = 20 * EUR
# 4. Write python docstrings for each function (I can show you examples separately)
# 5. Avoid writing elses where it is not needed:
# if a:
#   return a
# return b
# 6. No need to add type annotations for each variable
# Especially where it is obvious
# a: float = 1.2
# Usually it is good enough to just have type annotations only for function parameters and return values
# 7. Tests (more on that probably separately)

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
   if surcharge > 0:  # you can try to use function `max` here to avoid writing if's.
      return surcharge
   else: return 0. # return on a new line

    
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

def get_number_of_items_fee(number_of_items: int) -> int: # it is better to name functions without articles and short words like `the`, `a`, `of` etc. For example, `get_items_count_fee`
    min_number = 5 
    max_number = 12
    number_fee = 50
    extra_fee = 120

    if  number_of_items - max_number > 0 :  # number_of_items > max_number
        return (number_of_items - max_number) * number_fee + extra_fee
 
    if  number_of_items - min_number > 0 :  # number_of_items > min_number
        return (number_of_items - max_number) * number_fee
    
    else: return 0  # return on a new line. Else not needed
    

# delivery_date = datetime.now()
# weekday = delivery_date.weekday() # Note that weekdays start with zero. So friday will be 4
# current_hour = delivery_date.hour
def get_time_fee(time: str) -> float:  # you can expect that some date is coming here
    time_index: float = 1.2
    if time== 'friday':
        return time_index
    else: return 1  # return on a new line

# instead of time: str you can use datetime
# from datetime import datetime
# time: datetime
# Also, `time` is not good name for a variable, because built-in python module has same name
# You could use something like `delivery_date` for example
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
    else: delivery_fee  # no return added here 