def calculate_product(x,y):
    return x * y
def multiply_by_two(x):
    return calculate_product(x,2)
def multiply_by_three(x):
    return calculate_product(x,3)
result = multiply_by_two(multiply_by_three(4))
print(result)