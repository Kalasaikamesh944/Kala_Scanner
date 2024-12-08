import subprocess

def run_local_scan():
    print("[*] Running local system scan with Lynis...")
    subprocess.run(["sudo", "lynis", "audit", "system"])

def run_remote_scan(target):
    print(f"[*] Running remote system scan against {target} using Lynis...")
    
    # Step 1: Create tarball
    subprocess.run("mkdir -p ./files && cd .. && tar czf ./lynis/files/lynis-remote.tar.gz --exclude=files/lynis-remote.tar.gz ./lynis && cd lynis", shell=True)
    
    # Step 2: Copy tarball to remote target
    subprocess.run(f"scp -q ./files/lynis-remote.tar.gz {target}:~/tmp-lynis-remote.tgz", shell=True)
    
    # Step 3: Run Lynis audit on remote target
    subprocess.run(f"ssh {target} 'mkdir -p ~/tmp-lynis && cd ~/tmp-lynis && tar xzf ../tmp-lynis-remote.tgz && rm ../tmp-lynis-remote.tgz && cd lynis && ./lynis audit system'", shell=True)
    
    # Step 4: Clean up remote directory
    subprocess.run(f"ssh {target} 'rm -rf ~/tmp-lynis'", shell=True)
    
    # Step 5: Retrieve logs and report
    subprocess.run(f"scp -q {target}:/tmp/lynis.log ./files/{target}-lynis.log", shell=True)
    subprocess.run(f"scp -q {target}:/tmp/lynis-report.dat ./files/{target}-lynis-report.dat", shell=True)
    
    # Step 6: Clean up temp files
    subprocess.run(f"ssh {target} 'rm /tmp/lynis.log /tmp/lynis-report.dat'", shell=True)
    print(f"[*] Scan complete for {target}!")

