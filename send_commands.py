#!/usr/bin/python3

import paramiko
from getpass import getpass

# Get the username, password and the command that I want to run on the server
user = input('What user do you want to connect with? ')
passwd = getpass()
command = input('What command do you want to run? ')

# The list of the IP addresses that I need to connect to along with the port
device_list = (IP_ADDRESSES)
port = 22

# A loop to work through the above ip addresses to connect to them via ssh and then send the commands. Output is saved and exported to the screen
for device in device_list:
    print(f'Output from {device}:')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(device,port,user,passwd)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
    outlines = ssh_stdout.readlines()
    resp = ''.join(outlines)
    print(resp)
    ssh.close()
