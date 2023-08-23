import os
import time
import fileinput
import re

def add_ports_to_firewall(ports):
    ports_list = ports.split(",")
    for port in ports_list:
        os.system(f"ufw allow {port}/tcp")

# آپدیت
os.system("apt update -y && apt upgrade -y && apt install curl -y && apt install git -y && apt install screen -y && apt --fix-broken install")
os.system("clear")
print("Welcome To Mrkiller Script ! @Mr_Killer_1\n")

def banner():
    print("""
    [1] install BBR 
    [2] install warp
    [3] install security script
    [4] install security script2
    [5] install ssh connection encryption 
    [6] install firewall
    [7] install warp2
    \n""")
    m = input(">>> ")

    if m == '1':
        os.system("wget -N --no-check-certificate https://github.com/teddysun/across/raw/master/bbr.sh && chmod +x bbr.sh && bash bbr.sh")
        os.system("clear")
        time.sleep(3)
        print("Installed successfully!")
        banner()
    elif m == '2':
        os.system("bash <(curl -sSL https://raw.githubusercontent.com/hamid-gh98/x-ui-scripts/main/install_warp_proxy.sh)")
        os.system("clear")
        time.sleep(3)
        print("Installed successfully!")
        banner()
    elif m == '3':
        os.system("bash <(curl -s https://raw.githubusercontent.com/elemen3/wepn/master/wepn.sh)")
        os.system("clear")
        time.sleep(3)
        print("Installed successfully!")
        banner()
    elif m == '4':
        os.system("wget https://raw.githubusercontent.com/opiran-club/block-iran-ip/main/block-ip.sh && chmod +x block-ip.sh && ./block-ip.sh")
        os.system("clear")
        time.sleep(3)
        print("Installed successfully!")
        banner()
    elif m == '5':
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

        replace_ssh_cipher()
        os.system("clear")
        time.sleep(3)
        print("SSH encryption configuration completed successfully!")
        banner()
    elif m == '6':
        ports = input("Enter ports (e.g., 8080,9090,7629): ")
        add_ports_to_firewall(ports)
        os.system("clear")
        time.sleep(3)
        print("Firewall installed successfully!")
        banner()
    elif m == '7':
        os.system("bash <(curl -Ls https://gitlab.com/rwkgyg/CFwarp/raw/main/CFwarp.sh)")
        os.system("clear")
        time.sleep(3)
        print("Warp2 installed successfully!")
        banner()

while True:
    banner()
