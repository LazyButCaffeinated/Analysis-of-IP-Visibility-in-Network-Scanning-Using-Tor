🌐 Source IP Obfuscation in Network Scanning

A practical exploration of how proxy-routed scanning affects source IP visibility and scan behavior.

✨ Overview

This project explores how the source IP address observed by a target system changes when Nmap scan traffic is routed through a proxy (Tor) instead of being sent directly.

It focuses on network flow, IP visibility, and scan result behavior, while also providing persistent scan reports for analysis.

🔍 What This Project Demonstrates

How Nmap normally exposes the scanner’s source IP

How proxy routing alters the source IP seen by the target

Differences between:

Local packet capture (scanner-side)

Remote observation (target-side)

How proxy routing impacts scan accuracy

Automatic generation of human-readable scan reports

🧠 How It Works
Scanner (VM)
   ↓
Tor SOCKS Proxy
   ↓
Tor Exit Node (Public IP)
   ↓
Target System


Nmap traffic is routed through Tor using ProxyChains

The target system sees the Tor exit node IP

The scanner’s local IP appears only in local packet captures

🧰 Tools & Stack

Nmap – Network scanning

Tor – Proxy routing

ProxyChains – Traffic redirection

Wireshark – Packet analysis

Python – Automation & reporting

Kali Linux (VM) – Execution environment

🚀 Features

Proxy-routed TCP connect scanning (-sT)

Automatic Tor circuit rotation

Controlled, slow scanning behavior

Real-time terminal output

Automatic text report generation

Timestamped scan records for later review

📝 Scan Reports

Every scan automatically generates a clean text report.

📄 Report Includes

Scan timestamp

Target IP / domain

Ports scanned

Tor exit IPs used

Raw Nmap output per port

Summary of open ports

📁 Report Location
reports/
└── scan_report_YYYYMMDD_HHMMSS.txt

👀 Observations

Local packet captures show the private IP because traffic is captured before proxy routing

The target system sees only the Tor exit node IP

Scan traffic appears as encrypted TLS streams

Proxy-based scans against local (LAN) targets may produce false negatives

⚠️ Limitations

Proxy routing is unreliable for private (LAN) IP addresses

Proxy-based scans may miss open services

Tor traffic can be detected or filtered

Source IP obfuscation ≠ anonymity

📂 Repository Structure
.
├── script.py
├── reports/
│   └── scan_report_*.txt
└── README.md

▶️ Usage
sudo python3 script.py


Follow the prompts to enter:

Target IP / domain

Ports to scan

Reports are generated automatically after the scan completes.

🏁 Conclusion

This project highlights how proxy-based routing changes source IP visibility during network scans and how it affects scan accuracy.
It combines hands-on scanning, traffic analysis, and persistent reporting into a single, practical workflow.
