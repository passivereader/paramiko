from getpass import getpass
from pprint import pprint
import paramiko

# exception handling!
# better use netmiko for dealing with network devices
# https://ktbyers.github.io/netmiko/docs/netmiko/base_connection.html

def main():

    client = paramiko.client.SSHClient()

    client.load_system_host_keys()
    # client.__dict__
    # client._system_host_keys.__dict__

    client.connect(input("Enter hostname or IP: "), \
    username=input("Enter username: "), \
    password=getpass("Password (SSH key password if applicable): "), \
    timeout=2.0, \
    banner_timeout=2.0, \
    auth_timeout=2.0, \
    channel_timeout=2.0, \
    allow_agent=False)

    stdin, stdout, stderr = client.exec_command('show arp')
    raw_output_list = stdout.readlines()

    client.close()
    
    pprint(clean(raw_output_list))

def clean(raw_output_list=[]):
    cleaned = []
    for output_line in raw_output_list:
        cleaned.append(output_line.rstrip())
    even_cleaner = list(filter(None, cleaned))
    return even_cleaner

if __name__ == "__main__":
    main()
