import time
import requests  
from tabulate import tabulate

# Add the valid submdomains in the list to check the status.
subdomains = [
    "comcast.com",
    "omagle.com",
    "yahoo.com",
    #Add here for more
]

# Function to check subdomain status
def check_subdomain_status(subdomain):
    try:
        response = requests.get(f"https://{subdomain}", timeout=5)  
        response.raise_for_status()  
        return "Up"
    except requests.exceptions.RequestException as e:
        return f"Down ({e.__class__.__name__})"

# Infinite loop to continuously check and update status
while True:
    print("\033c")  

    # Check status for each subdomain and build table data
    table_data = []
    for subdomain in subdomains:
        status = check_subdomain_status(subdomain)
        table_data.append([subdomain, status])

    # Print updated table
    print(tabulate(table_data, headers=["Subdomain", "Status"], tablefmt="grid"))

    # Delay for half minute
    time.sleep(30)
