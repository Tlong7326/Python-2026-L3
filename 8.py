I = [ 1,4,5,-1,10]
def extract_even(I):
    even_numbers = []
    for num in I:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

even_list = extract_even(I)
print(even_list)