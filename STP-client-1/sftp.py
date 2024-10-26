import paramiko
from decouple import config

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
    sftp.chdir('/')
    
    files = sftp.listdir()
    print(files)

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'sftp' in locals():
        sftp.close()
    ssh.close()
    print("Disconnected from the SFTP server.")

