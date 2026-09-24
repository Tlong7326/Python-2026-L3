import math

num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("Please enter a non-negative integer.")
else:
    print(f"The factorial of {num} is {math.factorial(num)}")