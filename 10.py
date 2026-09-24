def get_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

num = int(input("Enter a number: "))
print(f"Divisors of {num}: {get_divisors(num)}")
