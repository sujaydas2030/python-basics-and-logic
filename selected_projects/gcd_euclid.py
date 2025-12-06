"""
File: gcd_euclid.py
Problem: Compute the Greatest Common Divisor (GCD) of two positive integers using Euclid's algorithm.
Author: Sujay Das
Approach:
- Use the efficient Euclidean algorithm (iterative).
"""

# Finding GCD
# Taking input
num1 = int(input("Enter the first positive number: "))
num2 = int(input("Enter the second positive number: "))

def gcd(a, b):
    # Write your code here
    while b:
        a, b = b, a % b
    return a

# Print the output
print(f"The GCD of {num1} and {num2} is: {gcd(num1, num2)}")

