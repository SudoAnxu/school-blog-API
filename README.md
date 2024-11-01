# Data Processing Assignment

A lightweight Python implementation for weather data processing and prime factorization, plus SQL query functionality. Built using only core Python features without external dependencies.

## Features

1. Weather Data Processing (`process_weather_data`)
   - Aggregates weather metrics by city
   - Handles missing data gracefully
   - Calculates averages for each metric
   ```python
   # Example input:
   records = [
       {'city': 'New York', 'temperature': 20.5, 'humidity': 65},
       {'city': 'New York', 'temperature': 22.0, 'humidity': None}
   ]
   ```

2. Prime Factorization (`prime_factorization`)
   - Converts integers into prime factors with exponents
   - Handles edge cases (numbers ≤ 1)
   ```python
   # Example:
   # Input: 60
   # Output: [(2, 2), (3, 1), (5, 1)]  # means 2^2 * 3^1 * 5^1
   ```

3. SQL Query
   - Updates product prices by 10%
   - Displays original and new prices
   - Orders results by product name

## Setup

No installation required! Just Python's standard library:
1. Ensure Python is installed on your system
2. Download `main.py` to your working directory

## Usage

1. Weather Data Processing:
```python
# Import function
from main import process_weather_data

# Prepare your data
weather_data = [
    {'city': 'London', 'temperature': 18.5, 'humidity': 70},
    {'city': 'London', 'temperature': 19.0}
]

# Get results
results = process_weather_data(weather_data)
```

2. Prime Factorization:
```python
from main import prime_factorization

# Get prime factors
factors = prime_factorization(60)  # Returns [(2, 2), (3, 1), (5, 1)]
```

3. SQL Query:
```sql
-- Execute in your SQL environment:
SELECT 
    name,
    price AS original_price,
    ROUND(price * 1.10, 2) AS new_price
FROM 
    products
ORDER BY 
    name;
```

## Testing

Run the included test cases:
```bash
python main.py
```

## Implementation Notes

- No external libraries used
- Built using only Python standard features
- Efficient prime factorization algorithm
- Handles missing data in weather records
- SQL query includes proper rounding to 2 decimal places

## Error Handling

- Weather data processing:
  - Skips invalid numeric values
  - Ignores records without city names
  - Handles missing metrics gracefully

- Prime factorization:
  - Returns empty list for inputs ≤ 1
  - Handles all positive integers
#   s c h o o l - b l o g - A P I  
 #   s c h o o l - b l o g - A P I  
 #   s c h o o l - b l o g - A P I  
 #   s c h o o l - b l o g - A P I  
 #   s c h o o l - b l o g - A P I  
 #   s c h o o l - b l o g - A P I  
 