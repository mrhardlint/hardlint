import sys
import os
import signal
import time
from colorama import init, Fore, Style
from modules import banner_art
from modules import domain_tools
from modules import network_tools
from modules import social_tools
from modules import vehicle_tools
from modules import crypto_tools
from modules import leak_tools

# Initialize colorama
init()

def signal_handler(sig, frame):
    print(f"\n{Fore.RED}[!] Exiting hardlint...{Style.RESET_ALL}")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_splash():
    clear_screen()
    splash_text = banner_art.get_splash()
    for line in splash_text.split('\n'):
        print(line)
        time.sleep(0.04)
    
    print(f"{Fore.YELLOW}Press ENTER to start...{Style.RESET_ALL}")
    input()
    clear_screen()
    print(banner_art.get_header())

def print_help():
    print(f"\n{Fore.YELLOW}Available Commands (Ultimate V2):{Style.RESET_ALL}")
    print(f"{Fore.BLUE}[Identity & Social]{Style.RESET_ALL}")
    print(f"  {Fore.GREEN}search <<username \"<name>\"{Style.RESET_ALL}   : Mass search on 100+ sites")
    print(f"  {Fore.GREEN}search <<email \"<email>\"{Style.RESET_ALL}      : Email analysis (Gravatar + Dorks)")
    print(f"  {Fore.GREEN}search <<number \"<phone>\"{Style.RESET_ALL}     : Phone reverse lookup")
    print(f"  {Fore.GREEN}search <<image \"<url>\"{Style.RESET_ALL}       : Reverse image search links")
    
    print(f"\n{Fore.BLUE}[Network & Domain]{Style.RESET_ALL}")
    print(f"  {Fore.GREEN}search <<ip \"<ip>\"{Style.RESET_ALL}           : IP Geolocation")
    print(f"  {Fore.GREEN}search <<mac \"<mac>\"{Style.RESET_ALL}         : MAC Address Vendor Lookup")
    print(f"  {Fore.GREEN}search <<domain \"<site.com>\"{Style.RESET_ALL} : WHOIS, DNS, Tech Stack, Subdomains")
    
    print(f"\n{Fore.BLUE}[Assets & Misc]{Style.RESET_ALL}")
    print(f"  {Fore.GREEN}search <<crypto \"<addr>\"{Style.RESET_ALL}     : Bitcoin/Eth Wallet Check")
    print(f"  {Fore.GREEN}search <<vin \"<vin>\"{Style.RESET_ALL}         : Vehicle VIN Decoder")
    print(f"  {Fore.GREEN}search <<leak \"<query>\"{Style.RESET_ALL}      : Search for leaks/pastes")

    print(f"\n  {Fore.GREEN}!help{Style.RESET_ALL}                         : Show this help message")
    print(f"  {Fore.GREEN}exit{Style.RESET_ALL}                          : Exit the tool")

def parse_search_command(cmd_str):
    try:
        parts = cmd_str.split("<<")
        if len(parts) < 2:
            return None, None
        rest = parts[1].strip()
        target_type = rest.split(" ")[0]
        start_quote = rest.find('"')
        end_quote = rest.rfind('"')
        if start_quote == -1 or end_quote == -1:
            return None, None
        value = rest[start_quote+1:end_quote]
        return target_type, value
    except:
        return None, None

def main():
    show_splash()
    
    while True:
        try:
            prompt = f"{Fore.BLUE}hardlint > {Style.RESET_ALL}"
            command = input(prompt).strip()
            
            if not command:
                continue
            if command == "exit":
                break
            if command == "!help":
                print_help()
                continue
                
            if command.startswith("search"):
                target_type, value = parse_search_command(command)
                if not target_type or not value:
                    print(f"{Fore.RED}[!] Invalid syntax. Use !help{Style.RESET_ALL}")
                    continue
                    
                print(f"{Fore.MAGENTA}---> Starting Module: {target_type.upper()} <---{Style.RESET_ALL}\n")
                
                if target_type == "username":
                    social_tools.search_username(value)
                elif target_type == "email":
                    social_tools.search_email(value)
                elif target_type == "number":
                    social_tools.search_number(value)
                elif target_type == "image":
                    social_tools.reverse_image_search(value)
                
                elif target_type == "ip":
                    network_tools.search_ip(value)
                elif target_type == "mac":
                    network_tools.mac_lookup(value)
                elif target_type == "domain":
                    domain_tools.get_whois(value)
                    domain_tools.get_dns_records(value)
                    domain_tools.detect_tech(value)
                    domain_tools.subdomain_scanner(value)
                    
                elif target_type == "crypto":
                    crypto_tools.check_crypto(value)
                elif target_type == "vin":
                    vehicle_tools.check_vin(value)
                elif target_type == "leak":
                    leak_tools.check_leaks(value)
                    
                else:
                    print(f"{Fore.RED}[!] Unknown search type: {target_type}{Style.RESET_ALL}")
                    
                print(f"\n{Fore.MAGENTA}---> Module Finished <---{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[!] Command not recognized.{Style.RESET_ALL}")

        except KeyboardInterrupt:
            print("\n")
            continue
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
