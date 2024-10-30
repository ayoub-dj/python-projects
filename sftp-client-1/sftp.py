import paramiko
from decouple import config
import os

HOST = config('SFTP_HOST', cast=str)
PORT = config('SFTP_PORT', cast=int)
USERNAME = config('SFTP_USERNAME', cast=str)
PASSWORD = config('SFTP_PASSWORD', cast=str)



ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(hostname=HOST, port=PORT, username=USERNAME, password=PASSWORD)
    print("Connected to the SFTP server.")
    
    sftp = ssh.open_sftp()

    path = '/home/conf/'
    sftp.chdir(path)

    files = sftp.listdir()
    print(files)

    remote_file = 'gunicorn_config.py'
    local_path = rf'{os.getcwd()}\sftp-client-1\conf.py'

    sftp.get(remotepath=remote_file, localpath=local_path)

    print('#' * 33)
    print(f'Downloaded {remote_file} to {local_path}')


except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'sftp' in locals():
        sftp.close()
    ssh.close()
    print("Disconnected from the SFTP server.")

