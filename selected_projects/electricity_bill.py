"""
File: electricity_bill.py
Problem: Calculate the electricity bill based on slab rates.
Author: Sujay Das
Approach:
- Slab rates: first 100 units @5/unit, next 100 units (101-200) @8/unit, above 200 @10/unit
- Return total payable (integer or float as required).
- Handles non-negative input and displays a helpful message for invalid values.
"""
# Taking input
units = int(input())
rate = 0

# Write your code here
if units <= 100:
    rate = 5
    total_spend = (units * rate)
elif 101 <= units <= 200:
    rate = 8
    total_spend = (100 * 5 + (units - 100) * rate)
else:
    rate = 10
    total_spend = (100 * 5 + 100 * 8 + (units - 200) * 10)

# Print the output
print(total_spend)
