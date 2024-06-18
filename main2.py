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
        print(f"Open ports for {ip}:")
        for port in host['ports']:
            print(f"- {port}")
    except shodan.APIError as e:
        print(f"Error: {e}")
