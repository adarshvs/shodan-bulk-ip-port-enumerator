import shodan

# Replace with your Shodan API key
API_KEY = 'YOUR_SHODAN_API_KEY'

# List of IP addresses to lookup
ip_list = ['192.168.1.1', '192.168.1.2', '192.168.1.3']

# Initialize Shodan API client
api = shodan.Shodan(API_KEY)

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
