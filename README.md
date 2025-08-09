D@rkNet Tools 🛠 — OSINT IP Information Tool

A simple command-line tool to perform OSINT (Open Source Intelligence) analysis on an IP address.  
The tool fetches detailed information about an IP, including location, provider, security flags, and more, using the [ipwho.is](http://ipwho.is) API and presents the data in a neat table format in the terminal.

---

## Features

- Queries IP information like city, region, country, ISP, continent, latitude, and longitude  
- Detects if the IP is using VPN, Proxy, TOR, or hosting services  
- Displays country flag emoji  
- Uses rich library for beautiful terminal output  
- Automatically opens a Telegram channel link on start

---

## Installation

Make sure you have Python 3 installed. Then install the required packages:

```
pip install requests rich
```
---

Usage

Run the script:
```
python IPSEARCH.py
```
Enter the IP address you want to analyze when prompted.

---

Example

Enter IP address for analysis: 8.8.8.8

🔍 Analyzing...

┌────────────┬──────────────┐
│ Field      │ Value        │
├────────────┼──────────────┤
│ IP         │ 8.8.8.8      │
│ City       │ Mountain View│
│ Region     │ California   │
│ Country    │ United States│
│ Provider   │ Google LLC   │
│ Continent  │ North America│
│ Flag       │ 🇺🇸           │
│ VPN / Proxy│ No           │
│ TOR        │ No           │
│ Hosting    │ No           │
│ Latitude   │ 37.4056      │
│ Longitude  │ -122.0775    │
└────────────┴──────────────┘


---

Author 

Owner: Ghostoraner
Connection: reinsss21@gmail.com 
