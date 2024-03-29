from getpass import getpass
from pprint import pprint
import paramiko

# exception handling!

def main():

    client = paramiko.client.SSHClient()

    client.load_system_host_keys()
    # client.__dict__
    # client._system_host_keys.__dict__
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    privkey_SSH_absolute_path = input("Absolute path to SSH private key: ")

    client.connect(input("Enter hostname or IP: "), \
    username=input("Enter username: "), \
    password=getpass("Password (SSH key passphrase if applicable): "), \
    key_filename=privkey_SSH_absolute_path, \
    timeout=2.0, \
    banner_timeout=2.0, \
    auth_timeout=2.0, \
    channel_timeout=2.0, \
    allow_agent=False)

    stdin, stdout, stderr = client.exec_command( \
    "echo 'missing cat after && creates stderr output' >> test_paramiko \
    && test_paramiko")

    raw_stdout_list = stdout.readlines() # will be an empty list
    raw_stderr_list = stderr.readlines()

    client.close()
    
    pprint(clean(raw_stdout_list))
    pprint(clean(raw_stderr_list))

def clean(raw_output_list=[]):
    cleaned = []
    for output_line in raw_output_list:
        cleaned.append(output_line.rstrip())
    even_cleaner = list(filter(None, cleaned))
    return even_cleaner

if __name__ == "__main__":
    main()
