# Quick Port Scan

`remote-port-scanner.py` is a lightweight Python script designed to rapidly scan common remote management and network service ports on one or multiple hosts. It is especially useful when traditional port scanners (like `nmap`) fail to produce results—such as environments with security appliances that block typical scanning methods.

## Features

- **Scans a curated list of popular remote management and service ports:** SSH, RDP, SNMP, printing, databases, and more.
- **Single IP or entire CIDR range support:** Scan individual hosts or subnets with one command.
- **Flexible port scanning methods:** Uses Bash `/dev/tcp` and Netcat (`nc`), optimizing for systems where certain tools may be unavailable or blocked.
- **No external Python port-scanning dependencies:** Relies on system utilities for fast, reliable checks.

## Why use Remote Port Scan?

- **When nmap is blocked or ineffective:** This script uses alternative system calls that often evade detection by firewalls/security appliances targeting traditional scanners.
- **Rapid, convenient checks:** Ideal for sysadmins, network engineers, and security teams.

## Usage

### Prerequisites

- Python 3.x
- Bash shell available on your system
- Netcat (`nc`) utility installed
    - On Debian/Ubuntu: `sudo apt-get install netcat`
    - On RHEL/CentOS: `sudo yum install nc`

### How to Run

1. Save the script as `remote-port-scanner.py`.
2. (Optional) Make it executable:  
   `chmod +x remote-port-scanner.py`
3. Run the script:

   ```bash
   python3 remote-port-scanner.py
   ```
   or (if made executable):
   ```bash
   ./remote-port-scanner.py
   ```

4. When prompted, enter either:
   - a single IP address (e.g., `192.168.1.10`)
   - or a CIDR network (e.g., `192.168.1.0/24`)

5. The script will display results for each host and port, indicating if each port is `OPEN` or `closed`.

### Example Output

```
Enter an IP or CIDR (e.g. 192.168.161.82 or 192.168.161.0/24): 192.168.1.10

===== Scanning 192.168.1.10 =====
Port 9100 is closed
Port 515 is closed
Port 631 is OPEN
...
```

## How It Works

- **Scan Logic**:
  1. Tries to connect using Bash's `/dev/tcp`.
  2. Falls back to Netcat (`nc`) if necessary.
  3. Reports port status as `OPEN` or `closed`.

## Default Ports Scanned

| Port | Service            |
|------|--------------------|
| 22   | SSH                |
| 23   | Telnet             |
| 443  | HTTPS              |
| 515  | LPD Print Service  |
| 631  | IPP Print Service  |
| 69   | TFTP               |
| 111  | RPCBind            |
| 123  | NTP                |
| 135  | Microsoft RPC      |
| 161  | SNMP               |
| 162  | SNMP Trap          |
| 389  | LDAP               |
| 445  | SMB                |
| 5900 | VNC                |
| 3389 | RDP                |
| 2049 | NFS                |
| 3306 | MySQL              |
| 5432 | PostgreSQL         |
| 636  | LDAPS              |
| 9100 | JetDirect Printing |
| 50000| SAP                |
| 5985 | WinRM (HTTP)       |
| 5986 | WinRM (HTTPS)      |

## Troubleshooting

- **Permission Errors:** Ensure you have access to run Bash and Netcat.
- **Missing Netcat:** Install `nc` with your OS package manager.
- **Firewall Restrictions:** Results only reflect what’s accessible from your machine.

## Customization

- To add or remove ports, simply edit the `PORTS` list in the script.
- The script can be extended to use additional port scanning methods if needed.

## Disclaimer

This tool is for ethical and administrative use only. **Do NOT use it to scan networks without proper authorization.**

---

**Author:**  
Dextan-solutions  
2025
