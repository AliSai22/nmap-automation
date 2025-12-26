import subprocess
from datetime import datetime
import sys
import os

if len(sys.argv) != 2:
    print("Usage: python3 nmap_scan.py <target>")
    sys.exit(1)

target = sys.argv[1]
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_dir = "output"
output_file = f"{output_dir}/scan_{timestamp}.txt"

os.makedirs(output_dir, exist_ok=True)

command = ["nmap", "-sV", "-Pn", target]

print(f"[*] Scanning {target}...")
with open(output_file, "w") as f:
    subprocess.run(command, stdout=f)

print(f"[+] Scan saved to {output_file}")
