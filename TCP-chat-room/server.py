import threading, socket
from decouple import config

host = config('SERVER_HOST', cast=str)
port = config('SERVER_PORT', cast=int)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []
lock = threading.Lock()
coder = 'ascii'

def broadcast(message):
    with lock:
        for client in clients:
            try:
                client.send(message)
            except Exception as e:
                print(f"Error sending message: {e}")

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            if message:
                broadcast(message)
            else:
                raise ConnectionError("Client disconnected.")
        except Exception as e:
            with lock:
                if client in clients:
                    index = clients.index(client)
                    clients.remove(client)
                    client.close()
                    nickname = nicknames[index]
                    broadcast('{} left!'.format(nickname).encode(coder))
                    nicknames.remove(nickname)
                    break

def receive():
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        client.send('NICK'.encode(coder))
        nickname = client.recv(1024).decode(coder)
        
        with lock:
            nicknames.append(nickname)
            clients.append(client)

        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode(coder))
        client.send('Connected to server!'.encode(coder))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


if __name__ == '__main__':
    receive()
