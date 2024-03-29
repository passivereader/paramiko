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

    privkey_SSH_abs_path = input("Absolute path to SSH private key: ")

    # ilo3 requires looong timeouts
    client.connect(input("Enter hostname or IP: "), \
    username=input("Enter username: "), \
    password=getpass("Password (SSH key passphrase if applicable): "), \
    key_filename=privkey_SSH_abs_path, \
    timeout=12.0, \
    banner_timeout=12.0, \
    auth_timeout=12.0, \
    channel_timeout=12.0, \
    allow_agent=False)

    start_stop_choice = input("""Hit Enter to confirm your choice:
    Press 0 to let ilo3 stop the server.
    Press 1 to let ilo3 start the server.
    Press anything else to do nothing and exit.
    Make your choice: """)

    if start_stop_choice == "0":
        start_stop_choice = "stop system1"
    elif start_stop_choice == "1":
        start_stop_choice = "start system1"
    else:
        print("Good bye.")
        client.close()
        exit()

    stdin, stdout, stderr = client.exec_command(start_stop_choice)

    raw_stdout_list = stdout.readlines()
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
