## Description 
An HTTP service designed for delivery fee calculation.  
The service is written using FastAPI.  
To calculate delivery fee send POST request to the following endpoint:  
```
POST /delivery_fee
```  
with the following JSON body:  
```json
{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2024-01-15T13:00:00Z"}
```

##### Field details

| Field             | Type  | Description                                                               | Example value                             |
|:---               |:---   |:---                                                                       |:---                                       |
|cart_value         |Integer|Value of the shopping cart __in cents__.                                   |__790__ (790 cents = 7.90€)                |
|delivery_distance  |Integer|The distance between the store and customer’s location __in meters__.      |__2235__ (2235 meters = 2.235 km)          |
|number_of_items    |Integer|The __number of items__ in the customer's shopping cart.                   |__4__ (customer has 4 items in the cart)   |
|time               |String |Order time in UTC in [ISO format](https://en.wikipedia.org/wiki/ISO_8601). |__2024-01-15T13:00:00Z__                   |

#### Response
Example:
```json
{"delivery_fee": 710}
```

##### Field details

| Field         | Type  | Description                           | Example value             |
|:---           |:---   |:---                                   |:---                       |
|delivery_fee   |Integer|Calculated delivery fee __in cents__.  |__710__ (710 cents = 7.10€)|

## Prerequisites
Python 3.11.7  
pip installed
## Installation
```
pip install -r requirements.txt
```
## Running the service
```
uvicorn app.main:app
```
The service will be started on http://127.0.0.1:8000 by default
## Testing 
```
pytest tests/*
```
## Notes
1. Test coverage is 100%
```
---------- coverage: platform darwin, python 3.11.7-final-0 ----------
Name                    Stmts   Miss  Cover
-------------------------------------------
app/fee_calculator.py      54      0   100%
app/main.py                14      0   100%
-------------------------------------------
TOTAL                      68      0   100%
```

2. No additional time zone convertions are made since date is always coming in UTC by specification 

3. Rush hour is checked using the following condition:  
```
15 <= current_hour < 19
```
because it is unclear whether 7PM should be included.  

4. Zero values for fields cart_value, delivery_distance, number_of_items are intentionally allowed. Only negative values are considered as invalid.  

5. The function rounds the delivery_fee up to integers since the result value in the response must be in type int.  