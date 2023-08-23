import subprocess
import time
import fileinput
import re

def add_ports_to_firewall(ports):
    ports_list = ports.split(",")
    for port in ports_list:
        subprocess.run(["ufw", "allow", f"{port}/tcp"])

def install_BBR():
    subprocess.run(["wget", "-N", "--no-check-certificate", "https://github.com/teddysun/across/raw/master/bbr.sh"])
    subprocess.run(["chmod", "+x", "bbr.sh"])
    subprocess.run(["bash", "bbr.sh"])

def install_warp():
    subprocess.run(["bash", "-c", "curl -sSL https://raw.githubusercontent.com/hamid-gh98/x-ui-scripts/main/install_warp_proxy.sh | bash"])

def replace_ssh_cipher():
    def replace_line(filepath, pattern, replacement):
        with fileinput.FileInput(filepath, inplace=True) as file:
            for line in file:
                updated_line = re.sub(pattern, replacement, line)
                print(updated_line, end='')

    sshd_config_file = '/etc/ssh/sshd_config'
    pattern = r'^# Ciphers and keying'
    replacement = 'Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes256-ctr'

    def check_line(filepath, pattern):
        with open(filepath, 'r') as file:
            return any(re.search(pattern, line) for line in file)

    if not check_line(sshd_config_file, replacement):
        replace_line(sshd_config_file, pattern, replacement)
        print("SSH encryption configuration completed successfully!")

menu = """
[1] install BBR 
[2] install warp
[3] install security script
[4] install security script2
[5] install ssh connection encryption 
[6] install firewall
[7] install warp2
[8] Exit
"""

print("Welcome To Mrkiller Script ! @Mr_Killer_1\n")
print(menu)

m = input(">>> ")

if m == '1':
    install_BBR()
elif m == '2':
    install_warp()
elif m == '3':
    subprocess.run(["bash", "-c", "curl -sSL https://raw.githubusercontent.com/elemen3/wepn/master/wepn.sh | bash"])
elif m == '4':
    subprocess.run(["wget", "https://raw.githubusercontent.com/opiran-club/block-iran-ip/main/block-ip.sh"])
    subprocess.run(["chmod", "+x", "block-ip.sh"])
    subprocess.run(["./block-ip.sh"])
elif m == '5':
    replace_ssh_cipher()
elif m == '6':
    ports = input("Enter ports (e.g., 8080,9090,7629): ")
    add_ports_to_firewall(ports)
    print("Firewall installed successfully!")
elif m == '7':
    subprocess.run(["bash", "-c", "curl -Ls https://gitlab.com/rwkgyg/CFwarp/raw/main/CFwarp.sh | bash"])
elif m == '8':
    pass
