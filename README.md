# Automated Subnet & Network Scanner

A lightweight, multithreaded Python CLI tool designed for network engineers and security analysts to perform rapid host discovery and TCP port scanning across target CIDR subnets.

## Features

- **CIDR Subnet Parsing:** Uses standard library tools to automatically calculate valid host IP addresses in any subnet (e.g., `/24`, `/28`).
- **Multithreaded Execution:** Utilizes thread pools (`ThreadPoolExecutor`) to scan hundreds of IP addresses and ports simultaneously within seconds.
- **Port & Service Identification:** Probes target TCP ports and maps open ports to standard networking service names (e.g., HTTP, HTTPS, SSH, RDP).
- **JSON Report Generation:** Export scan findings directly to structured JSON files for documentation, SIEM ingestion, or subsequent auditing.
- **Zero External Dependencies:** Built entirely with Python standard libraries (`socket`, `ipaddress`, `threading`, `argparse`).

## Repository Structure

```text
network-scanner/
│── README.md
│── scanner.py
└── requirements.txt
