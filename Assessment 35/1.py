def apply_function_to_list(lst, func):

    return [func(x) for x in lst]


# Define a function to double a number
def double(x):
    return x * 2

# Define a function to square a number
def square(x):
    return x ** 2

# List of integers
numbers = [1, 2, 3, 4, 5]

# Apply the 'double' function to each element in the list
doubled_numbers = apply_function_to_list(numbers, double)
print("Doubled numbers:", doubled_numbers)

# Apply the 'square' function to each element in the list
squared_numbers = apply_function_to_list(numbers, square)
print("Squared numbers:", squared_numbers)