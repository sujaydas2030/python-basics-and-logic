"""
File: gcd_euclid.py
Problem: Compute the Greatest Common Divisor (GCD) of two positive integers using Euclid's algorithm.
Author: Sujay Das
Approach:
- Use the efficient Euclidean algorithm (iterative).
- Handles edge-cases like zeros.
"""

def gcd(a: int, b: int) -> int:
    """Return GCD of a and b using Euclid's algorithm."""
    a, b = abs(a), abs(b)
    if a == 0:
        return b
    if b == 0:
        return a
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    # Example interactive usage:
    try:
        num1 = int(input("Enter first positive integer: ").strip())
        num2 = int(input("Enter second positive integer: ").strip())
    except ValueError:
        print("Please enter valid integers.")
    else:
        print(f"GCD of {num1} and {num2} is: {gcd(num1, num2)}")
