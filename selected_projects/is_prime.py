# Taking input
num = int(input())

def is_prime(n):
    # Write your code
    if n <= 1:
        return "Not Prime"
    if n == 2:
        return "Prime"
    if n % 2 == 0:
        return "Not Prime"
    # Check for odd divisors from 3 up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return "Not Prime"
    return "Prime"

# Print the output
print(is_prime(num))
