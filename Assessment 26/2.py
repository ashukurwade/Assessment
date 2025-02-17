# import sys

# def main():
#     try:
#         # Extract command-line arguments, excluding the script name
#         numbers = [int(arg) for arg in sys.argv[1:]]
        
#         if not numbers:
#             print("Error: No numbers provided. Please enter at least one integer.")
#             return
        
#         # Sort numbers in descending order
#         sorted_numbers = sorted(numbers, reverse=True)
        
#         # Print top 3 largest numbers (handle fewer than 3 inputs)
#         top_numbers = sorted_numbers[:3]
#         print("Top 3 largest numbers:", " ".join(map(str, top_numbers)))

#     except ValueError:
#         print("Error: Please provide only integer values.")

# if __name__ == "__main__":
#     main()


import sys

def main():
    # Check if at least 3 integers are provided
    if len(sys.argv) < 4:
        print("Error: Please provide at least 3 integers.")
        return

    # Extract integers from command-line arguments
    try:
        numbers = [int(arg) for arg in sys.argv[1:]]
    except ValueError:
        print("Error: All arguments must be valid integers.")
        return

    # Sort the integers in descending order
    sorted_numbers = sorted(numbers, reverse=True)

    # Print the top 3 largest integers
    print("Top 3 largest integers:")
    for num in sorted_numbers[:3]:
        print(num)

if __name__ == "__main__":
    main()