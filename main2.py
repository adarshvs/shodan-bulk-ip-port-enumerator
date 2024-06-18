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
        
        # Extract and print open ports
        result = f"Open ports for {ip}:\n"
        for port in host['ports']:
            result += f"- {port}\n"
        
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
