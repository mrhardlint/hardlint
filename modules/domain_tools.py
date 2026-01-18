import whois
import dns.resolver
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
import time

def get_whois(domain):
    print(f"{Fore.CYAN}[*] Performing WHOIS lookup for: {domain}{Style.RESET_ALL}")
    try:
        w = whois.whois(domain)
        print(f"{Fore.GREEN}[+] Registrar: {w.registrar}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[+] Creation Date: {w.creation_date}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[+] Expiration Date: {w.expiration_date}{Style.RESET_ALL}")
        if w.emails:
            print(f"{Fore.GREEN}[+] Emails: {w.emails}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] WHOIS failed: {e}{Style.RESET_ALL}")

def get_dns_records(domain):
    print(f"\n{Fore.CYAN}[*] Retrieving DNS Records...{Style.RESET_ALL}")
    record_types = ['A', 'MX', 'NS', 'TXT', 'CNAME']
    
    for r_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, r_type)
            for rdata in answers:
                print(f"{Fore.BLUE}[~] {r_type}: {rdata.to_text()}{Style.RESET_ALL}")
        except dns.resolver.NoAnswer:
            pass
        except Exception:
            pass

def detect_tech(url):
    if not url.startswith('http'):
        url = 'http://' + url
        
    print(f"\n{Fore.CYAN}[*] Detecting Technology stack for: {url}{Style.RESET_ALL}")
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Headers check
        server = response.headers.get('Server')
        if server:
             print(f"{Fore.GREEN}[+] Server: {server}{Style.RESET_ALL}")
             
        x_powered = response.headers.get('X-Powered-By')
        if x_powered:
             print(f"{Fore.GREEN}[+] Powered By: {x_powered}{Style.RESET_ALL}")

        # Meta tags check
        meta_gen = soup.find("meta", attrs={"name": "generator"})
        if meta_gen:
            print(f"{Fore.GREEN}[+] Generator (CMS): {meta_gen.get('content')}{Style.RESET_ALL}")
            
    except Exception as e:
        print(f"{Fore.RED}[!] Tech detection failed: {e}{Style.RESET_ALL}")

def subdomain_scanner(domain):
    print(f"\n{Fore.CYAN}[*] Scanning for subdomains (crt.sh)...{Style.RESET_ALL}")
    try:
        url = f"https://crt.sh/?q=%.{domain}&output=json"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            subs = set()
            for entry in data:
                name_value = entry['name_value']
                # Handle multi-line entries
                for sub in name_value.split('\n'):
                    subs.add(sub)
            
            print(f"{Fore.GREEN}[+] Found {len(subs)} unique subdomains:{Style.RESET_ALL}")
            count = 0
            for sub in subs:
                if count < 15: # Limit output to avoid flooding
                    print(f"{Fore.BLUE}    - {sub}{Style.RESET_ALL}")
                count += 1
            if count > 15:
                print(f"{Fore.YELLOW}    ...and {count-15} more.{Style.RESET_ALL}")
    except Exception as e:
         print(f"{Fore.RED}[!] Subdomain scan failed: {e}{Style.RESET_ALL}")
