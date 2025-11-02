# Shodan Bulk IP Port Enumerator
This Python script uses the Shodan API to scan a list of IP addresses for open ports and logs the results into a CSV file. The script processes each IP one by one, printing the results in the terminal as it scans and immediately saving them into a CSV file.


### Features:
<p>  •	Real-time Output: Displays the open ports for each IP in the terminal as the scan progresses.
<p>  •	Immediate Logging: Saves each IP's results to a CSV file (output.csv) right after processing.
<p>  •	Error Handling: Logs IPs without available data and handles unexpected errors gracefully.
<p>  •	Formatted CSV Output: Ports are listed neatly under the corresponding IP in the CSV file.
  
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
python shodan_to_csv_and_terminal.py
```

## Output
The script creates or appends to an output.txt file in the same directory. This file contains the open ports for each IP address or error messages if the lookup fails.



"""
shodan_subnet_enum_live_excel_resume.py

Fetch Shodan InternetDB info for each IP in a subnet and
write results to Excel line-by-line (with resume support and retry-safe saving).

Requirements:
    pip install requests pandas openpyxl
"""
