def apply_functions_in_sequence(numbers, functions):
    """
    Applies each function in the list `functions` to the list `numbers` in sequence.
    
    :param numbers: List of numbers to be processed.
    :param functions: List of functions to be applied in sequence.
    :return: List of numbers after applying all functions in sequence.
    """
    result = numbers  # Start with the original list of numbers
    
    for func in functions:
        result = [func(x) for x in result]  # Apply the current function to each number in the list
    
    return result

# Example usage:

# Define some functions
def add_one(x):
    return x + 1

def square(x):
    return x ** 2

def subtract_ten(x):
    return x - 10

# List of numbers
numbers = [1, 2, 3, 4, 5]

# List of functions to apply
functions = [add_one, square, subtract_ten]

# Apply the functions in sequence
final_result = apply_functions_in_sequence(numbers, functions)

print(final_result)  # Output: [-8, -5, 0, 7, 16]