Source IP Obfuscation in Network Scanning
Overview

This project demonstrates how the source IP address visible to a target system changes when Nmap scan traffic is routed through a proxy (Tor) instead of being sent directly.

The project focuses on:

Network traffic flow

Source IP visibility

Differences between local packet capture and target-side observation

Report generation for scan results

How It Works
Scanner (VM)
   ↓
Tor SOCKS Proxy
   ↓
Tor Exit Node (Public IP)
   ↓
Target System


Nmap traffic is routed through Tor using ProxyChains

The target system sees the Tor exit node IP as the source

The scanner’s local IP is visible only at the local capture point (Wireshark)

Tools Used

Nmap

Tor

ProxyChains

Wireshark

Python

Kali Linux (Virtual Machine)

Features

Proxy-routed Nmap TCP connect scanning

Automatic Tor circuit changes during scans

Controlled and slow scanning behavior

Real-time scan output in terminal

Automatic text report generation

Timestamped scan reports

Scan Reports

After each scan, a text report is automatically generated and saved.

Report Contents

Scan timestamp

Target IP / domain

Ports scanned

Tor exit IPs used during the scan

Raw Nmap output per port

Summary of open ports

Report Location
reports/
└── scan_report_YYYYMMDD_HHMMSS.txt

Observations

Wireshark on the scanner shows the local private IP because capture happens before proxy routing

The target system sees only the Tor exit node IP

Scan traffic appears as encrypted TLS traffic

Proxy-based scans against local network targets may show open ports as closed or filtered

Limitations

Proxy routing does not work reliably for private (LAN) IP addresses

Proxy-based scans can produce false negatives

Tor traffic can be detected or blocked

Source IP obfuscation does not imply anonymity

Repository Structure
.
├── script.py
├── reports/
│   └── scan_report_*.txt
└── README.md

Example Usage
sudo python3 script.py


Follow the prompts to enter:

Target IP / domain

Ports to scan

Conclusion

This project shows how routing network scans through a proxy affects source IP visibility and scan behavior.
It also demonstrates how scan data can be stored in structured text reports for later analysis.
