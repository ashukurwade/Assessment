import argparse

def filter_logs(file_path, error_level):

    try:
        with open(file_path, 'r') as file:
            for line in file:
                if error_level in line:
                    print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Filter logs by error level.")
    parser.add_argument('file_path', type=str, help='Path to the log file')
    parser.add_argument('error_level', type=str, help='Error level to filter (e.g., INFO, WARN, ERROR)')

    # Parse arguments
    args = parser.parse_args()

    # Filter and display logs
    filter_logs(args.file_path, args.error_level)

if __name__ == "__main__":
    main()