from ftplib import FTP
from decouple import config
import os

HOST = config('FTP_HOST', cast=str)
USER = config('FTP_USERNAME', cast=str)
PASSWORD = config('FTP_PASSWORD', cast=str)


def upload_file(ftp, file):
    with open(file, 'rb') as f:
        ftp.storbinary('STOR requirements.txt', f)

def download_file(ftp, file):
    with open(rf'{os.getcwd()}\ftp-client-1\from_s.txt', 'wb') as f:
        ftp.retrbinary(f'RETR {file}', f.write)


def main():
    with FTP(HOST) as ftp:
        ftp.login(user=USER, passwd=PASSWORD)

        print(ftp.getwelcome())

        upload_file(ftp, rf'{os.getcwd()}\requirements.txt')
        download_file(ftp, 'x.txt')


if __name__ == '__main__':
    main()