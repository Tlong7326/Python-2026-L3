number = int(input("Enter a positive integer: "))

if number > 0:
    divisor_sum = sum(
        divisor for divisor in range(1, number) if number % divisor == 0
    )
    if divisor_sum == number:
        print(f"{number} is a perfect number.")
    else:
        print(f"{number} is NOT a perfect number.")
else:
    print("Please enter a positive integer.")