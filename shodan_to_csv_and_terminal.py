import shodan
import csv

# Replace with your Shodan API key
API_KEY = 'shodan_api_key'

# Initialize Shodan API client
api = shodan.Shodan(API_KEY)

# Read the list of IP addresses from a text file
with open('ip_list.txt', 'r') as file:
    ip_list = file.read().splitlines()

# Create the CSV file and write the header only once
with open('output.csv', 'w', newline='') as csvfile:
    fieldnames = ['IP', 'Ports']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

# Process each IP one by one and save immediately
for ip in ip_list:
    with open('output.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['IP', 'Ports'])
        
        try:
            # Perform Shodan IP lookup
            host = api.host(ip)

            # Extract open ports with transport
            ports = []
            for service in host.get('data', []):
                port = service.get('port')
                transport = service.get('transport', '').upper()
                ports.append(f"{port}/{transport}")

            # Format the output
            formatted_ports = '\n'.join(ports)
            result = f"Open ports for {ip}:\n{formatted_ports if formatted_ports else 'None'}\n"

            # Print the result to the terminal
            print(result)

            # Write the IP and ports to the CSV
            writer.writerow({'IP': ip, 'Ports': formatted_ports})

        except shodan.APIError as e:
            # Handle specific case where no information is available
            if "No information available for that IP" in str(e):
                error_message = f"Error: No information available for that IP ({ip})."
                print(error_message)
                writer.writerow({'IP': ip, 'Ports': ''})
            else:
                error_message = f"Error: {e} ({ip})."
                print(error_message)
                writer.writerow({'IP': ip, 'Ports': f"Error: {e}"})

        except Exception as e:
            # Handle any other exceptions
            error_message = f"Unexpected error for {ip}: {str(e)}"
            print(error_message)
            writer.writerow({'IP': ip, 'Ports': f"Unexpected error: {str(e)}"})
