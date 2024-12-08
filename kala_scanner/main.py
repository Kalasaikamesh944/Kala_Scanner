import argparse
import os
import sys
from colorama import init, Fore
from modules import network_scanner, web_scanner, system_scanner
from integration import report_generator, notifications

# Initialize colorama
init(autoreset=True)

# ASCII Hacker Banner
def print_hacker_banner():
    banner = """
    ██████╗ █████╗ ███████╗██╗  ██╗████████╗███████╗
    ██╔══██╗██╔══██╗██╔════╝██║  ██║╚══██╔══╝██╔════╝
    ██████╔╝███████║███████╗███████║   ██║   █████╗  
    ██╔═══╝ ██╔══██║╚════██║██╔══██║   ██║   ██╔══╝  
    ██║     ██║  ██║███████║██║  ██║   ██║   ███████╗
    ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝
    """
    print(Fore.GREEN + banner)

def main():
    print_hacker_banner()

    parser = argparse.ArgumentParser(description="Hacker-themed All-in-One Vulnerability Monitoring Tool")
    parser.add_argument('--target', type=str, help="URL, IP, or DNS to scan (e.g., http://example.com or 192.168.1.1)")
    parser.add_argument('--network', action='store_true', help="Perform network scanning (e.g., Nmap, OpenVAS)")
    parser.add_argument('--web', action='store_true', help="Perform web application scanning (e.g., OWASP ZAP)")
    parser.add_argument('--system', action='store_true', help="Perform system vulnerability scanning (e.g., Lynis)")
    parser.add_argument('--report', type=str, help="Generate a report (HTML or PDF)")
    parser.add_argument('--notify', type=str, help="Send notifications (e.g., email or Slack)")
    parser.add_argument('--local', action='store_true', help="Run local system scan")
    args = parser.parse_args()

    if not args.target and not args.local:
        print(Fore.RED + "[ERROR] You must specify a target (URL, IP, or DNS) with --target, or run a local scan with --local")
        sys.exit(1)

    if args.target:
        print(Fore.CYAN + f"[*] Target: {args.target}")

    if args.network:
        print(Fore.YELLOW + "[*] Running network scan...")
        network_scanner.run(args.target)

    if args.web:
        print(Fore.YELLOW + "[*] Running web scan...")
        web_scanner.run(args.target)

    if args.system:
        if args.local:
            print(Fore.YELLOW + "[*] Running Local System Scan...")
            system_scanner.run_local_scan()
        else:
            print(Fore.YELLOW + "[*] Running Remote System Scan...")
            system_scanner.run_remote_scan(args.target)

    if args.report:
        print(Fore.YELLOW + f"[*] Generating {args.report} report...")
        report_generator.create(args.report)

    if args.notify:
        print(Fore.YELLOW + f"[*] Sending notification to {args.notify}...")
        notifications.send(args.notify)

if __name__ == "__main__":
    main()
