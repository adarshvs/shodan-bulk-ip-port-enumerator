import shodan

# Replace with your Shodan API key
API_KEY = 'YOUR_SHODAN_API_KEY'

# Initialize Shodan API client
api = shodan.Shodan(API_KEY)

# Read the list of IP addresses from a text file
with open('ip_list.txt', 'r') as file:
    ip_list = file.read().splitlines()

# Loop through each IP address
for ip in ip_list:
    try:
        # Perform Shodan IP lookup
        host = api.host(ip)

        # Extract and print open ports with transport
        ports = []
        for service in host.get('data', []):
            port = service.get('port')
            transport = service.get('transport', '').upper()
            ports.append(f"{port}/{transport}")

        # Format the result as a comma-separated list
        result = f"Open ports for {ip}:\n{', '.join(ports)}\n"

        # Print and save the result
        print(result)
        with open('output.txt', 'a') as output_file:
            output_file.write(result)
    except shodan.APIError as e:
        # Handle specific case where no information is available
        if "No information available for that IP" in str(e):
            error_message = f"Error: No information available for that IP ({ip}).\n"
        else:
            error_message = f"Error: {e} ({ip}).\n"
        
        print(error_message)
        with open('output.txt', 'a') as output_file:
            output_file.write(error_message)
    except Exception as e:
        # Handle any other exceptions, including unparseable JSON
        error_message = f"Unexpected error for {ip}: {str(e)}\n"
        print(error_message)
        with open('output.txt', 'a') as output_file:
            output_file.write(error_message)
