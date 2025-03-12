# You need to check if numbers in a large list are prime.
# Instead of checking them one by one (which is slow), use multiprocessing to speed up the process.

#  Create a function to check if a number is prime.
#  Use multiprocessing.Pool.map() to divide the task across multiple CPU cores.
#  Return a list of prime numbers from the input list.

import multiprocessing

# Define the is_prime function at the top level
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_parallel(numbers):
    """Find prime numbers in a list using multiprocessing."""
    with multiprocessing.Pool() as pool:
        # Use the is_prime function to check each number in parallel
        results = pool.map(is_prime, numbers)
    
    # Return the numbers that are prime
    return [num for num, is_prime in zip(numbers, results) if is_prime]

if __name__ == "__main__":
    # Example list of numbers
    numbers = list(range(1, 1000001))

    # Find prime numbers using multiprocessing
    primes = find_primes_parallel(numbers)

    # Print the first 10 prime numbers found
    print("First 10 prime numbers found:", primes[:10])