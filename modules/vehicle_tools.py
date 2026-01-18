import requests
from colorama import Fore, Style

def check_vin(vin):
    print(f"{Fore.CYAN}[*] Decoding VIN: {vin}{Style.RESET_ALL}")
    url = f"https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/{vin}?format=json"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        results = data.get('Results', [])
        
        found_info = False
        for item in results:
            value = item.get('Value')
            variable = item.get('Variable')
            if value and value != "null":
                # Filter for interesting fields
                if variable in ["Make", "Model", "Model Year", "Plant City", "Manufacturer Name", "Vehicle Type", "Body Class", "Engine Number of Cylinders", "Fuel Type - Primary"]:
                    print(f"{Fore.GREEN}[+] {variable}: {value}{Style.RESET_ALL}")
                    found_info = True
        
        if not found_info:
             print(f"{Fore.RED}[!] Could not decode VIN (or invalid VIN).{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}[!] VIN lookup failed: {e}{Style.RESET_ALL}")
