import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor

# Common ports and their standard network services
COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP"
}

def check_port(ip_address, port):
    """Tries to connect to a specific IP and port. Returns service name if open."""
    try:
        # Create a basic TCP socket connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Wait max 0.5 seconds for a response
        
        result = sock.connect_ex((str(ip_address), port))
        sock.close()
        
        if result == 0:  # 0 means port is OPEN
            service_name = COMMON_PORTS.get(port, "Unknown")
            return port, service_name
    except Exception:
        pass
    
    return None

def scan_single_ip(ip_address, ports_to_scan):
    """Scans all requested ports on one IP address."""
    open_ports = []
    
    for port in ports_to_scan:
        res = check_port(ip_address, port)
        if res:
            open_ports.append(res)
            
    if open_ports:
        print(f"[+] Active Host Discovered: {ip_address}")
        for port, service in open_ports:
            print(f"    └── Port {port} ({service}) is OPEN")
        print("-" * 40)

def main():
    # --- CONFIGURATION (CHANGE THESE IF NEEDED) ---
    target_subnet = "127.0.0.1/32"  # Scans your local computer first to guarantee output
    ports_to_check = [21, 22, 80, 443, 445, 3389]
    

    print("=" * 40)
    print("      AUTOMATED NETWORK SCANNER          ")
    print("=" * 40)
    print(f"[*] Target Subnet : {target_subnet}")
    print(f"[*] Ports to Scan : {ports_to_check}")
    print("[*] Scanning... Please wait.\n")

    # Generate list of IP addresses from CIDR network block
    network = ipaddress.ip_network(target_subnet, strict=False)
    all_ips = list(network.hosts())
    
    # If network has no host range (like a single /32 IP), use the main address
    if not all_ips:
        all_ips = [network.network_address]

    # Use multithreading so scanning is fast
    with ThreadPoolExecutor(max_workers=20) as executor:
        for ip in all_ips:
            executor.submit(scan_single_ip, ip, ports_to_check)

    print("[*] Scan completed successfully!")

if __name__ == "__main__":
    main()