# HARDLINT ULTIMATE (V2) 🕵️‍♂️

**HARDLINT** is a professional-grade, modular OSINT (Open Source Intelligence) framework designed for researchers, penetration testers, and privacy enthusiasts. It aggregates data from over 100+ public sources to build comprehensive digital profiles.

![Hardlint Logo](https://via.placeholder.com/800x200?text=HARDLINT+ULTIMATE+V2)

## 🚀 New V2 Features

### 🌐 Domain & Network OSINT
- **Massive Domain Analysis**: WHOIS data, DNS record dumps (A, MX, TXT, etc.), and Technology Stack detection (CMS, Server).
- **Subdomain Scanner**: Passive enumeration using transparency logs (Certificate Transparency).
- **IP Geolocation**: Pinpoint location with Country, City, ISP, and Google Maps integration.
- **MAC Lookup**: Identify device manufacturers from MAC addresses.

### 🕵️‍♂️ Identity & Social
- **Username Search (Turbo)**: Multi-threaded scanning of **100+ social networks** (TikTok, GitHub, Tinder, Roblox, etc.) in seconds.
- **Reverse Image Search**: Generates direct deep-links for Google Lens, Yandex, TinEye, and Bing Visual Search.
- **Email Forensics**: Automatic Gravatar detection and specialized Google Dorks for manual breach/leak discovery.

### 💰 Financial & Physical Assets
- **Crypto Analysis**: Check Bitcoin (BTC) and Ethereum (ETH) wallet balances, transaction counts, and total received funds.
- **Vehicle Intelligence**: Decode VIN numbers to reveal Make, Model, Year, Plant City, and Engine specs.

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/hardlint.git
   cd hardlint
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the tool:**
   ```bash
   python hardlint.py
   ```

## 📖 Command Reference

Once started, use the following interactive commands:

| Domain | Command | Description |
| :--- | :--- | :--- |
| **Identity** | `search <<username "name"` | Search 100+ sites for username. |
| | `search <<email "addr"` | Analyze email for leaks & profile pics. |
| | `search <<number "num"` | Reverse phone number lookup. |
| | `search <<image "url"` | Reverse image search links. |
| **Network** | `search <<ip "1.2.3.4"` | Geolocate IP address. |
| | `search <<mac "00:11..."` | Lookup MAC address vendor. |
| | `search <<domain "site.com"` | WHOIS, DNS, & Subdomains. |
| **Assets** | `search <<crypto "addr"` | Check Crypto Wallet balance. |
| | `search <<vin "1HG..."` | Decode Vehicle VIN. |
| **Misc** | `search <<leak "query"` | Search for password leaks/pastes. |

## 🛡️ Privacy & Ethics
This tool is for **educational and research purposes only**. Always respect local laws and the privacy of others. The developer is not responsible for any misuse of this tool.

---
*Made with ❤️ for the OSINT community.*
