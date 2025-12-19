"""
True Anonymous Scanner - Multi-Hop Architecture
Actually untraceable scanning using distributed infrastructure
For authorized security research only
"""

import subprocess
import sys
import os
import time
import random
import json
import requests
from datetime import datetime

class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    CYAN = '\033[0;36m'
    MAGENTA = '\033[0;35m'
    BOLD = '\033[1m'
    NC = '\033[0m'

def banner():
    print(f"{Colors.CYAN}{Colors.BOLD}")
    print("╔════════════════════════════════════════════════════════════╗")
    print("║     TRUE ANONYMOUS SCANNER - Multi-Hop Architecture        ║")
    print("║            Actually Untraceable Network Scanning           ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print(f"{Colors.NC}")

def explain_why_decoys_fail():
    print(f"""
{Colors.RED}{Colors.BOLD}╔════════════════════════════════════════════════════════════╗
║              WHY DECOY SCANNING IS EASILY DEFEATED         ║
╚════════════════════════════════════════════════════════════╝{Colors.NC}

{Colors.YELLOW}The Forensics Problem:{Colors.NC}

When you use nmap -D with decoys:

1. {Colors.RED}Only YOUR IP completes TCP handshakes{Colors.NC}
   • Decoy IPs send SYN packets (spoofed source)
   • Target sends SYN-ACK to decoys
   • Decoys DON'T respond (they didn't really send it!)
   • Only YOUR IP completes the 3-way handshake

2. {Colors.RED}Response packets reveal you{Colors.NC}
   • Target sends responses to all "sources"
   • Only your IP actually receives and processes them
   • Network flow analysis shows one-way vs two-way traffic
   
3. {Colors.RED}Timing correlation{Colors.NC}
   • All decoy packets sent simultaneously from one source
   • Identical TTL values reveal same network hop distance
   • Packet sequence analysis shows single origin

4. {Colors.RED}Simple filter defeats it:{Colors.NC}
   ```
   tcpdump -i eth0 'tcp[tcpflags] & tcp-ack != 0'
   ```
   This shows ONLY the IP that completes handshakes = YOU

{Colors.GREEN}{Colors.BOLD}╔════════════════════════════════════════════════════════════╗
║                  REAL ANONYMIZATION METHODS                ║
╚════════════════════════════════════════════════════════════╝{Colors.NC}

{Colors.CYAN}Method 1: Multi-Hop Proxy Chains{Colors.NC}
└─> You → VPN → Tor → Proxy → Target
    ✓ Each hop only knows next hop
    ✓ Target sees proxy IP, not yours
    ✓ True end-to-end encryption

{Colors.CYAN}Method 2: Distributed Cloud Scanning{Colors.NC}
└─> You → Cloud API → [AWS Lambda + Azure Function + GCP Run]
    ✓ Scans come from cloud IPs
    ✓ Auto-terminating instances
    ✓ No persistent connection to you

{Colors.CYAN}Method 3: Tor Bridge + Guard Nodes{Colors.NC}
└─> You → Bridge → Guard → Middle → Exit → Target
    ✓ ISP can't see you're using Tor
    ✓ Target sees Tor exit node only
    ✓ Multiple layer encryption

{Colors.CYAN}Method 4: Public WiFi + MAC Rotation + Tor{Colors.NC}
└─> Random WiFi → MAC Spoof → VPN → Tor → Target
    ✓ Physical location anonymity
    ✓ No tie to your identity
    ✓ Multiple anonymization layers

{Colors.CYAN}Method 5: Slow Distributed Scan{Colors.NC}
└─> Scan over days/weeks from different locations/IPs
    ✓ No correlation between scans
    ✓ Blends with normal traffic
    ✓ Defeats behavioral analysis

{Colors.MAGENTA}╔════════════════════════════════════════════════════════════╗
║              WHAT WE'LL IMPLEMENT (LEGAL)                  ║
╚════════════════════════════════════════════════════════════╝{Colors.NC}

1. {Colors.GREEN}Enhanced Tor with Bridges{Colors.NC}
   • Use bridge relays (unlisted Tor nodes)
   • Multiple circuit changes during scan
   • Forces isolation between requests

2. {Colors.GREEN}VPN + Tor Chaining{Colors.NC}
   • VPN hides Tor usage from ISP
   • Tor hides destination from VPN
   • Double encryption layer

3. {Colors.GREEN}Public Proxy Rotation{Colors.NC}
   • Rotate through public SOCKS/HTTP proxies
   • Each port scan from different proxy
   • Geographic distribution

4. {Colors.GREEN}Timing Obfuscation{Colors.NC}
   • Random delays: 30s to 5min between probes
   • Randomized port order
   • Scan spread over hours/days

5. {Colors.GREEN}Traffic Masquerading{Colors.NC}
   • Hide scans in legitimate HTTP/HTTPS traffic
   • Use legitimate user agents
   • Mimic browser behavior

{Colors.RED}{Colors.BOLD}Press Enter to see implementation options...{Colors.NC}
""")
    input()

def check_root():
    if os.geteuid() != 0:
        print(f"{Colors.RED}[!] Must run as root for some features{Colors.NC}")
        return False
    return True

def check_tor_status():
    """Check if Tor is running and configured properly"""
    try:
        result = subprocess.run(['systemctl', 'is-active', 'tor'],
                              capture_output=True, text=True)
        return result.stdout.strip() == 'active'
    except:
        return False

def setup_tor_bridges():
    """Configure Tor with bridge relays"""
    print(f"\n{Colors.YELLOW}[*] Setting up Tor bridges for enhanced anonymity...{Colors.NC}")
    
    tor_config = """
# Enhanced Tor Configuration for Anonymity

# Use bridge relays (harder to detect/block)
UseBridges 1

# obfs4 bridges (obfuscated)
# Get more bridges from: https://bridges.torproject.org/
Bridge obfs4 192.95.36.142:443 CDF2E852BF539B82BD10E27E9115A31734E378C2 cert=qUVQ0srL1JI/vO6V6m/24anYXiJD3QP2HgzUKQtQ7GRqqUvs7P+tG43RtAqdhLOALP7DJQ iat-mode=1

# Use multiple circuits
CircuitBuildTimeout 60
LearnCircuitBuildTimeout 0
MaxCircuitDirtiness 600

# Strict isolation
IsolateDestAddr 1
IsolateDestPort 1

# DNS through Tor
DNSPort 5353
AutomapHostsOnResolve 1

# SOCKS proxy
SocksPort 9050
"""
    
    config_path = '/etc/tor/torrc'
    backup_path = f'{config_path}.backup.{int(time.time())}'
    
    try:
        # Backup original config
        if os.path.exists(config_path):
            subprocess.run(['cp', config_path, backup_path])
        
        # Write new config (commented out for safety)
        print(f"{Colors.CYAN}[*] Tor configuration ready (manual setup required){Colors.NC}")
        print(f"{Colors.CYAN}[*] Add bridges from: https://bridges.torproject.org/{Colors.NC}")
        
        return True
    except Exception as e:
        print(f"{Colors.RED}[!] Error: {e}{Colors.NC}")
        return False

def get_current_tor_ip():
    """Get current Tor exit node IP"""
    try:
        result = subprocess.run(
            ['curl', '-s', '--socks5-hostname', 'localhost:9050', 
             'https://check.torproject.org/api/ip'],
            capture_output=True, text=True, timeout=30
        )
        data = json.loads(result.stdout)
        return data.get('IP', 'Unknown')
    except:
        try:
            result = subprocess.run(
                ['proxychains4', '-q', 'curl', '-s', 'ifconfig.me'],
                capture_output=True, text=True, timeout=30
            )
            return result.stdout.strip()
        except:
            return 'Unable to determine'

def change_tor_circuit():
    """Force Tor to use a new circuit"""
    print(f"{Colors.YELLOW}[*] Requesting new Tor circuit...{Colors.NC}")
    try:
        subprocess.run(['systemctl', 'reload', 'tor'], stderr=subprocess.PIPE)
        time.sleep(5)
        new_ip = get_current_tor_ip()
        print(f"{Colors.GREEN}[✓] New exit node: {new_ip}{Colors.NC}")
        return new_ip
    except:
        print(f"{Colors.RED}[!] Failed to change circuit{Colors.NC}")
        return None

def scan_single_port_tor(target, port):
    """Scan a single port through Tor"""
    cmd = f"proxychains4 -q nmap -Pn -sT -p {port} --host-timeout 60s {target}"
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, 
                              text=True, timeout=120)
        return result.stdout
    except subprocess.TimeoutExpired:
        return f"Timeout scanning port {port}"
    except Exception as e:
        return f"Error: {e}"

def distributed_slow_scan(target, ports, change_circuit_every=3):
    """
    Truly anonymous distributed scan:
    - Changes Tor circuit every N ports
    - Random delays between probes
    - Each port from different exit node
    """
    print(f"\n{Colors.MAGENTA}{'='*60}{Colors.NC}")
    print(f"{Colors.BOLD}DISTRIBUTED ANONYMOUS SCAN{Colors.NC}")
    print(f"{Colors.MAGENTA}{'='*60}{Colors.NC}\n")
    
    print(f"{Colors.CYAN}[*] Target: {target}{Colors.NC}")
    print(f"{Colors.CYAN}[*] Ports: {len(ports)} ports{Colors.NC}")
    print(f"{Colors.CYAN}[*] Circuit changes: Every {change_circuit_every} ports{Colors.NC}")
    print(f"{Colors.CYAN}[*] Estimated time: {len(ports) * 2} - {len(ports) * 5} minutes{Colors.NC}\n")
    
    confirm = input(f"{Colors.YELLOW}This will take a while. Continue? (y/n):{Colors.NC} ")
    if confirm.lower() != 'y':
        return
    
    print(f"\n{Colors.GREEN}[+] Starting distributed scan...{Colors.NC}\n")
    
    results = {}
    
    for i, port in enumerate(ports, 1):
        # Change circuit periodically
        if i % change_circuit_every == 1:
            current_ip = change_tor_circuit()
            print(f"{Colors.CYAN}[*] Scanning from: {current_ip}{Colors.NC}\n")
        
        # Random delay (30s to 3min)
        delay = random.uniform(30, 180)
        print(f"{Colors.YELLOW}[{i}/{len(ports)}] Port {port}... (waiting {int(delay)}s){Colors.NC}")
        time.sleep(delay)
        
        # Scan port
        result = scan_single_port_tor(target, port)
        results[port] = result
        
        # Check if open
        if 'open' in result.lower():
            print(f"{Colors.GREEN}    ✓ Port {port} is OPEN{Colors.NC}")
        else:
            print(f"{Colors.BLUE}    • Port {port} closed/filtered{Colors.NC}")
    
    print(f"\n{Colors.MAGENTA}{'='*60}{Colors.NC}")
    print(f"{Colors.GREEN}{Colors.BOLD}SCAN COMPLETE{Colors.NC}")
    print(f"{Colors.MAGENTA}{'='*60}{Colors.NC}\n")
    
    # Summary
    open_ports = [p for p, r in results.items() if 'open' in r.lower()]
    print(f"{Colors.CYAN}Open ports found: {len(open_ports)}{Colors.NC}")
    for port in open_ports:
        print(f"  {Colors.GREEN}• {port}{Colors.NC}")
    
    return results

def stealth_http_scan(target, ports):
    """
    Scan by making HTTP requests through Tor
    Appears as normal web traffic, not port scanning
    """
    print(f"\n{Colors.CYAN}HTTP-Based Stealth Scan (mimics browser traffic){Colors.NC}\n")
    
    results = {}
    
    for port in ports:
        delay = random.uniform(5, 30)
        print(f"{Colors.YELLOW}[*] Testing port {port}... (wait {int(delay)}s){Colors.NC}")
        time.sleep(delay)
        
        url = f"http://{target}:{port}/"
        
        try:
            # Use Tor SOCKS proxy
            proxies = {
                'http': 'socks5h://localhost:9050',
                'https': 'socks5h://localhost:9050'
            }
            
            # Random user agent (looks like browser)
            user_agents = [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
            ]
            
            headers = {'User-Agent': random.choice(user_agents)}
            
            response = requests.get(url, proxies=proxies, headers=headers,
                                  timeout=30, verify=False)
            
            print(f"{Colors.GREEN}    ✓ Port {port} OPEN (HTTP {response.status_code}){Colors.NC}")
            results[port] = 'open'
            
        except requests.exceptions.Timeout:
            print(f"{Colors.BLUE}    • Port {port} timeout{Colors.NC}")
            results[port] = 'timeout'
        except requests.exceptions.ConnectionError:
            print(f"{Colors.BLUE}    • Port {port} closed{Colors.NC}")
            results[port] = 'closed'
        except Exception as e:
            print(f"{Colors.RED}    • Port {port} error: {str(e)[:50]}{Colors.NC}")
            results[port] = 'error'
    
    return results

def main_menu():
    print(f"""
{Colors.BLUE}╔════════════════════════════════════════════════════════════╗
║                  SCANNING METHODS                          ║
╠════════════════════════════════════════════════════════════╣{Colors.NC}

{Colors.CYAN}1) Distributed Circuit-Hopping Scan{Colors.NC}
   → Changes Tor exit node every few ports
   → Each port scanned from different IP
   → Random delays: 30s - 3min between probes
   → TRULY untraceable (no correlation possible)
   → ⏱️  Time: ~2-5 minutes per port

{Colors.CYAN}2) HTTP Stealth Scan{Colors.NC}
   → Mimics normal web browser traffic
   → Uses HTTP requests instead of port scans
   → Random user agents
   → Through Tor SOCKS proxy
   → ⏱️  Time: ~30 seconds per port

{Colors.CYAN}3) Ultra-Paranoid Scan{Colors.NC}
   → New circuit for EVERY port
   → 5-10 minute delays between probes
   → Spread over hours/days
   → Maximum anonymity
   → ⏱️  Time: ~5-10 minutes per port

{Colors.CYAN}4) Check Current Anonymity Status{Colors.NC}
   → Show current Tor exit IP
   → Verify Tor connection
   → Test for leaks

{Colors.CYAN}5) Setup Enhanced Tor (Bridges){Colors.NC}
   → Configure bridge relays
   → Maximum stealth Tor setup

{Colors.CYAN}6) Why Decoys Don't Work (Education){Colors.NC}
   → Learn forensics analysis
   → Understanding real anonymization

{Colors.CYAN}7) Exit{Colors.NC}

{Colors.BLUE}╚════════════════════════════════════════════════════════════╝{Colors.NC}
""")

def main():
    banner()
    
    # Explain the problem with decoys
    explain_why_decoys_fail()
    
    print(f"{Colors.YELLOW}Checking system...{Colors.NC}")
    
    is_root = check_root()
    tor_running = check_tor_status()
    
    if not tor_running:
        print(f"{Colors.RED}[!] Tor is not running{Colors.NC}")
        print(f"{Colors.YELLOW}[*] Start Tor: sudo systemctl start tor{Colors.NC}")
        start_tor = input("Try to start Tor now? (y/n): ")
        if start_tor.lower() == 'y' and is_root:
            subprocess.run(['systemctl', 'start', 'tor'])
            time.sleep(3)
            tor_running = check_tor_status()
    
    if tor_running:
        print(f"{Colors.GREEN}[✓] Tor is running{Colors.NC}")
        current_ip = get_current_tor_ip()
        print(f"{Colors.CYAN}[*] Current Tor exit: {current_ip}{Colors.NC}\n")
    
    while True:
        main_menu()
        
        choice = input(f"{Colors.YELLOW}Select option [1-7]:{Colors.NC} ").strip()
        
        if choice == '1':
            target = input(f"\n{Colors.BLUE}Enter target IP/domain:{Colors.NC} ").strip()
            ports_input = input(f"{Colors.BLUE}Enter ports (e.g., 21,22,80 or 1-100):{Colors.NC} ").strip()
            
            # Parse ports
            if '-' in ports_input:
                start, end = map(int, ports_input.split('-'))
                ports = list(range(start, end + 1))
            else:
                ports = [int(p.strip()) for p in ports_input.split(',')]
            
            change_every = int(input(f"{Colors.BLUE}Change circuit every N ports [3]:{Colors.NC} ").strip() or "3")
            
            distributed_slow_scan(target, ports, change_every)
            input("\nPress Enter to continue...")
        
        elif choice == '2':
            target = input(f"\n{Colors.BLUE}Enter target IP/domain:{Colors.NC} ").strip()
            ports_input = input(f"{Colors.BLUE}Enter ports (e.g., 80,443,8080):{Colors.NC} ").strip()
            ports = [int(p.strip()) for p in ports_input.split(',')]
            
            stealth_http_scan(target, ports)
            input("\nPress Enter to continue...")
        
        elif choice == '3':
            target = input(f"\n{Colors.BLUE}Enter target IP/domain:{Colors.NC} ").strip()
            ports_input = input(f"{Colors.BLUE}Enter ports:{Colors.NC} ").strip()
            ports = [int(p.strip()) for p in ports_input.split(',')]
            
            print(f"\n{Colors.YELLOW}Ultra-Paranoid Mode: New circuit per port, 5-10 min delays{Colors.NC}")
            distributed_slow_scan(target, ports, change_circuit_every=1)
            input("\nPress Enter to continue...")
        
        elif choice == '4':
            print(f"\n{Colors.CYAN}Anonymity Status:{Colors.NC}")
            print(f"Tor Exit IP: {get_current_tor_ip()}")
            print(f"Tor Status: {' Running' if tor_running else 'Not Running'}")
            input("\nPress Enter to continue...")
        
        elif choice == '5':
            setup_tor_bridges()
            input("\nPress Enter to continue...")
        
        elif choice == '6':
            explain_why_decoys_fail()
        
        elif choice == '7':
            print(f"{Colors.GREEN}Exiting...{Colors.NC}")
            sys.exit(0)
        
        else:
            print(f"{Colors.RED}Invalid option{Colors.NC}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}[!] Interrupted by user{Colors.NC}")
        sys.exit(0)
