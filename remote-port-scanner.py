#!/usr/bin/env python3

import subprocess
import ipaddress

# Ports to scan
PORTS = [
    9100, 515, 631, 161, 162, 22, 23, 3389, 5900, 443,
    5985, 5986, 50000, 123, 69, 2049, 3306, 5432,
    389, 636, 445, 135, 111
]

def scan_port(host, port):
    """
    Try scanning using /dev/tcp first.
    If that fails, fallback to netcat.
    Returns True if open, False otherwise.
    """

    # First try /dev/tcp (bash)
    bash_cmd = f"echo > /dev/tcp/{host}/{port}"
    result = subprocess.run(
        ["bash", "-c", bash_cmd],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if result.returncode == 0:
        return True

    # Fallback to netcat
    nc_cmd = ["nc", "-z", "-w", "1", host, str(port)]
    result = subprocess.run(
        nc_cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return result.returncode == 0


def main():
    target = input("Enter an IP or CIDR (e.g. 192.168.161.82 or 192.168.161.0/24): ").strip()

    try:
        # Expand IP or CIDR
        network = ipaddress.ip_network(target, strict=False)
        hosts = [str(ip) for ip in network.hosts()]
    except ValueError:
        print("Invalid IP/CIDR format")
        return

    for host in hosts:
        print(f"\n===== Scanning {host} =====")
        for port in PORTS:
            if scan_port(host, port):
                print(f"Port {port} is OPEN")
            else:
                print(f"Port {port} is closed")


if __name__ == "__main__":
    main()
