# Shodan Bulk IP Port Enumerator
This repository contains a Python script that performs IP lookups using the Shodan API, retrieves information about open ports for a list of IP addresses, and writes the results to an output file.

### Prerequisites
Before running the script, ensure you have the following:

<p>  1. Python 3.x: The script requires Python 3.x to run.</p>

<p>  2. Shodan API Key: You need a valid Shodan API key to access the Shodan API. You can obtain one by creating an account on the Shodan website.</p>

<p>  3. Shodan Python Library: Install the Shodan Python library using pip:</p>

```bash
pip install shodan
```
### Usage
*   Clone the Repository:

```bash
git clone https://github.com/yourusername/shodan-ip-lookup.git
cd shodan-ip-lookup
```

*   Create IP List File:

Create a text file named ip_list.txt in the same directory as the script. This file should contain one IP address per line.

*   Update API Key:

Replace YOUR_SHODAN_API_KEY in the script with your actual Shodan API key:

```
API_KEY = 'YOUR_SHODAN_API_KEY'
```

*   Run the Script:

Execute the script using Python:

```bash
python shodan_ip_lookup.py
```

## Output
The script creates or appends to an output.txt file in the same directory. This file contains the open ports for each IP address or error messages if the lookup fails.
