import threading, socket 
from decouple import config

nickname = input("Choose your nickname: ")
host = config('SERVER_HOST', cast=str)
port = config('SERVER_PORT', cast=int)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except Exception as e:
            print(f"An error occurred: {e}")
            client.close()
            break

def write():
    while True:
        try:
            message = f"{nickname}: {input('')}"
            client.send(message.encode('ascii'))
        except Exception as e:
            print(f"Failed to send message: {e}")
            client.close()
            break

if __name__ == '__main__':
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()
