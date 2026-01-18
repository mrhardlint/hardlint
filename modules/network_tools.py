import requests
from colorama import Fore, Style

def search_ip(ip_address):
    ip_address = ip_address.strip()
    print(f"{Fore.CYAN}[*] Geolocation for IP: {ip_address}{Style.RESET_ALL}")
    
    api_url = f"http://ip-api.com/json/{ip_address}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query"
    
    try:
        response = requests.get(api_url, timeout=5)
        
        if response.status_code == 429:
             print(f"{Fore.RED}[!] Error: Rate limit exceeded for IP API. Try again later.{Style.RESET_ALL}")
             return
        if response.status_code != 200:
             print(f"{Fore.RED}[!] API Error: Server returned status code {response.status_code}{Style.RESET_ALL}")
             return

        try:
            data = response.json()
        except Exception:
            print(f"{Fore.RED}[!] Error: Invalid response from API. (Are you connected to the internet?){Style.RESET_ALL}")
            return
        
        if data['status'] == 'fail':
            err_msg = data.get('message', 'Unknown error')
            if err_msg == 'reserved range':
                print(f"{Fore.YELLOW}[!] This is a Private/Local IP (Reserved Range).{Style.RESET_ALL}")
                print(f"    Private IPs (like 192.168.x.x or 10.x.x.x) are used only inside your local Wi-Fi/LAN.")
                print(f"    They do not have a geographic location on the public internet.")
            else:
                print(f"{Fore.RED}[!] Failed to locate IP: {err_msg}{Style.RESET_ALL}")
            return

        print(f"\n{Fore.GREEN}[+] Location Data:{Style.RESET_ALL}")
        print(f"    - Country: {data['country']} ({data['countryCode']})")
        print(f"    - Region: {data['regionName']} ({data['region']})")
        print(f"    - City: {data['city']}")
        print(f"    - ZIP: {data['zip']}")
        print(f"    - Timezone: {data['timezone']}")
        print(f"    - Coordinates: {data['lat']}, {data['lon']}")
        
        print(f"\n{Fore.GREEN}[+] Network Data:{Style.RESET_ALL}")
        print(f"    - ISP: {data['isp']}")
        print(f"    - Org: {data['org']}")
        print(f"    - AS: {data['as']}")
        
        print(f"\n{Fore.BLUE}[~] Google Maps: https://www.google.com/maps/search/?api=1&query={data['lat']},{data['lon']}{Style.RESET_ALL}")
        
    except Exception as e:
        print(f"{Fore.RED}[!] Error connecting to IP geolocation service: {e}{Style.RESET_ALL}")

def mac_lookup(mac_address):
    print(f"{Fore.CYAN}[*] Looking up MAC Address: {mac_address}{Style.RESET_ALL}")
    try:
        url = f"https://api.macvendors.com/{mac_address}"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            print(f"{Fore.GREEN}[+] Vendor/Manufacturer: {response.text}{Style.RESET_ALL}")
        else:
             print(f"{Fore.RED}[!] Vendor not found or API limit reached.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] MAC lookup failed: {e}{Style.RESET_ALL}")
