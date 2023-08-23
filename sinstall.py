import subprocess
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

def install_security_script():
    subprocess.run(["bash", "-c", "bash <(curl -s https://raw.githubusercontent.com/elemen3/wepn/master/wepn.sh)"])

def install_security_script2():
    subprocess.run(["wget", "https://raw.githubusercontent.com/opiran-club/block-iran-ip/main/block-ip.sh"])
    subprocess.run(["chmod", "+x", "block-ip.sh"])
    subprocess.run(["./block-ip.sh"])

def install_warp2():
    subprocess.run(["bash", "-c", "bash <(curl -Ls https://gitlab.com/rwkgyg/CFwarp/raw/main/CFwarp.sh)"])

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

def main_menu():
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
    
    # تعریف تمام اسکریپت‌ها در یک لیست
    all_scripts = [
        install_BBR,
        install_warp,
        install_security_script,
        install_security_script2,
        replace_ssh_cipher,
        add_ports_to_firewall,
        install_warp2
    ]
    
    while True:
        print("Welcome To Mrkiller Script ! @Mr_Killer_1\n")
        print(menu)
        m = input(">>> ")

        if m == '8':
            break
        elif m.isdigit() and 1 <= int(m) <= len(all_scripts):
            script_index = int(m) - 1
            selected_script = all_scripts[script_index]
            selected_script()  # اجرای اسکریپت مربوط به گزینه انتخاب شده
        else:
            print("Invalid option. Please select a valid option from the menu.")

if __name__ == "__main__":
    main_menu()
