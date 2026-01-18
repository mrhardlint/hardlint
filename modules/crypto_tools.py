import requests
from colorama import Fore, Style
import re

def check_crypto(address):
    print(f"{Fore.CYAN}[*] Analyzing Crypto Wallet Address: {address}{Style.RESET_ALL}")
    
    # Simple Regex checks
    if re.match(r"^[13][a-km-zA-Z1-9]{25,34}$", address) or re.match(r"^bc1[a-zA-Z0-9]{39,59}$", address):
        currency = "Bitcoin (BTC)"
        explorer = f"https://www.blockchain.com/explorer/addresses/btc/{address}"
        api_url = f"https://blockchain.info/rawaddr/{address}"
    elif re.match(r"^0x[a-fA-F0-9]{40}$", address):
        currency = "Ethereum (ETH) / EVM"
        explorer = f"https://etherscan.io/address/{address}"
        api_url = None # Etherscan requires API key for raw data usually, keeping it simple
    else:
        print(f"{Fore.RED}[!] Unknown address format or not supported.{Style.RESET_ALL}")
        return

    print(f"{Fore.GREEN}[+] Detected Chain: {currency}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}[~] Explorer: {explorer}{Style.RESET_ALL}")
    
    if currency == "Bitcoin (BTC)":
        try:
            r = requests.get(api_url, timeout=5)
            if r.status_code == 200:
                data = r.json()
                total_received = data.get('total_received', 0) / 100000000
                final_balance = data.get('final_balance', 0) / 100000000
                n_tx = data.get('n_tx', 0)
                print(f"{Fore.GREEN}[+] Transactions: {n_tx}{Style.RESET_ALL}")
                print(f"{Fore.GREEN}[+] Total Received: {total_received} BTC{Style.RESET_ALL}")
                print(f"{Fore.GREEN}[+] Current Balance: {final_balance} BTC{Style.RESET_ALL}")
        except:
            print(f"{Fore.RED}[!] Could not fetch live balance (API limitation). Check explorer link.{Style.RESET_ALL}")
