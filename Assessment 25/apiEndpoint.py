import argparse
import requests
import sys

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Interact with web API")
    parser.add_argument('--api-key', required=True, help="API key for authentication")
    parser.add_argument('--endpoint', required=True, help="API endpoint URL")
    parser.add_argument('--params', nargs='*', help="Parameters as key-value pairs")
    args = parser.parse_args()

    # Validate API key
    if not args.api_key:
        print("Error: API key cannot be empty.", file=sys.stderr)
        sys.exit(1)

    # Validate endpoint
    if not args.endpoint.startswith(('http://', 'https://')):
        print("Error: Endpoint must be a valid URL starting with http:// or https://", file=sys.stderr)
        sys.exit(1)

    # Parse parameters into a dictionary
    params = {}
    if args.params:
        for param in args.params:
            if '=' not in param:
                print(f"Error: Invalid parameter format: {param}. Expected key=value.", file=sys.stderr)
                sys.exit(1)

            key, value = param.split('=', 1)
            params[key] = value  # Corrected assignment

    # Make the API request
    try:
        headers = {'Authorization': f'Bearer {args.api_key}'}
        response = requests.get(args.endpoint, headers=headers, params=params)
        response.raise_for_status()
        print("API Response:", response.json())

    except requests.exceptions.RequestException as e:  # Corrected exception name
        print(f"Error: Failed to make API request. {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()