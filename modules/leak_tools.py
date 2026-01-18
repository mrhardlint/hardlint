from colorama import Fore, Style

def check_leaks(query):
    print(f"{Fore.CYAN}[*] Searching for Leaks/Pastes for: {query}{Style.RESET_ALL}")
    
    print(f"{Fore.YELLOW}[!] Note: Direct searching of Pastebin/DeepWeb requires paid APIs or is blocked.{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[!] Generating specialized search links (Dorks) to find data manually:{Style.RESET_ALL}")
    
    dorks = [
        f"site:pastebin.com \"{query}\"",
        f"site:ghostbin.com \"{query}\"",
        f"site:justpaste.it \"{query}\"",
        f"inurl:pastebin \"{query}\"",
        f"filetype:txt \"{query}\" (password | email | user)",
        f"site:github.com \"{query}\" password",
        f"site:gitlab.com \"{query}\" password"
    ]
    
    for dork in dorks:
        link = f"https://www.google.com/search?q={dork.replace(' ', '+').replace('\"', '%22')}"
        print(f"{Fore.BLUE}[~] Search: {link}{Style.RESET_ALL}")

    print(f"\n{Fore.GREEN}[+] Also check these free breach databases:{Style.RESET_ALL}")
    print(f"{Fore.BLUE}[~] Leak-Lookup: https://leak-lookup.com/search?type=email&query={query}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}[~] BreachDirectory: https://breachdirectory.org/{Style.RESET_ALL}")
