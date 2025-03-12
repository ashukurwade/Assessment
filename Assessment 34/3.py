def apply_function_to_list(func, numbers):
    results = []
    for number in numbers:
        try:
            # Apply the function to the current number
            result = func(number)
            results.append(result)
        except Exception as e:
            # Handle the error and optionally log it
            print(f"Error applying function to {number}: {e}")
            results.append(None)  # Append None or some placeholder for failed cases
    return results


# Define a function that might throw an error for certain inputs
def safe_divide(x):
    return 10 / x

# List of numbers, including zero which will cause a division by zero error
numbers = [1, 2, 0, 4, 5]

# Apply the safe_divide function to the list
results = apply_function_to_list(safe_divide, numbers)

print(results)  # Output: [10.0, 5.0, None, 2.5, 2.0]