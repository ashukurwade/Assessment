# 2 Your task is to create a command-line tool that reads a list of integers passed as arguments and computes their sum and average.
# How would you handle potential errors, such as non-numeric values or incorrect number formats, and ensure that the program functions as expected?

import argparse
import sys

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Compute the sum and average of a list of integers.")
    parser.add_argument('numbers', nargs='+', help="List of integers to process")

    # Parse arguments
    args = parser.parse_args()

    # Validate and convert input to integers
    try:
        numbers = [int(num) for num in args.numbers]
    except ValueError:
        print("Error: All arguments must be valid integers.", file=sys.stderr)
        sys.exit(1)

    # Compute sum and average
    total = sum(numbers)
    average = total / len(numbers)

    # Output results
    print(f"Sum: {total}")
    print(f"Average: {average}")

if __name__ == "__main__":
    main()