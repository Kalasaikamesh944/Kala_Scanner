import subprocess
from colorama import Fore


def run(target):
    print(f"[*] Starting network scan against {target} using Nmap...")
    try:
        command = ["nmap", "-sV","-Pn", target]
        result = subprocess.run(command, stdout=subprocess.PIPE, text=True)
        print(f"{Fore.BLUE} {result.stdout}")
    except Exception as e:
        print(f"[ERROR] Error running network scan: {e}")
