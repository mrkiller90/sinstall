import os
import fileinput
import re

def add_ports_to_firewall(ports):
    ports_list = ports.split(",")
    for port in ports_list:
        os.system(f"ufw allow {port}/tcp")

def install_BBR():
    os.system("wget -N --no-check-certificate https://github.com/teddysun/across/raw/master/bbr.sh")
    os.system("chmod +x bbr.sh")
    os.system("bash bbr.sh")

def install_warp():
    os.system("bash <(curl -sSL https://raw.githubusercontent.com/hamid-gh98/x-ui-scripts/main/install_warp_proxy.sh)")

def replace_ssh_cipher():
    def replace_line(filepath, pattern, replacement):
        for line in fileinput.input(filepath, inplace=True):
            updated_line = re.sub(pattern, replacement, line)
            print(updated_line, end='')

    sshd_config_file = '/etc/ssh/sshd_config'
    pattern = r'^# Ciphers and keying'
    replacement = 'Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes256-ctr'

    def check_line(filepath, pattern):
        for line in fileinput.input(filepath):
            if re.search(pattern, line):
                return True
        return False

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

while True:
    print("Welcome To Mrkiller Script ! @Mr_Killer_1\n")
    print(menu)
    
    m = input(">>> ")

    if m == '1':
        install_BBR()
    elif m == '2':
        install_warp()
    elif m == '3':
        os.system("bash <(curl -sSL https://raw.githubusercontent.com/elemen3/wepn/master/wepn.sh)")
    elif m == '4':
        os.system("wget https://raw.githubusercontent.com/opiran-club/block-iran-ip/main/block-ip.sh")
        os.system("chmod +x block-ip.sh")
        os.system("./block-ip.sh")
    elif m == '5':
        replace_ssh_cipher()
    elif m == '6':
        ports = input("Enter ports (e.g., 8080,9090,7629): ")
        add_ports_to_firewall(ports)
        print("Firewall installed successfully!")
    elif m == '7':
        os.system("bash <(curl -Ls https://gitlab.com/rwkgyg/CFwarp/raw/main/CFwarp.sh)")
    elif m == '8':
        break
