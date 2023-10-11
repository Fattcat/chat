import socket
import threading

# Slovník pre uchovanie pripojených používateľov a ich mena
connected_clients = {}

def handle_client(client_socket):
    # Pripojenie používateľa
    client_name = client_socket.recv(1024).decode()
    connected_clients[client_name] = client_socket

    # Informovanie o pripojení používateľa
    print(f"{client_name} sa pripojil")

    # Zobraziť online používateľov
    display_online_users()

    while True:
        recipient_name = client_socket.recv(1024).decode()
        message = client_socket.recv(1024).decode()

        if recipient_name in connected_clients:
            recipient_socket = connected_clients[recipient_name]
            recipient_socket.send(f"{client_name}: {message}".encode())
        else:
            print(f"Odosielateľ {client_name} nenašiel príjemcu {recipient_name}")

def display_online_users():
    online_users = ", ".join(connected_clients.keys())
    print(f"ONLINE používatelia: {online_users}")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', 12345)
    server_socket.bind(server_address)
    server_socket.listen(5)

    print("Server čaká na pripojenie klientov...")

    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
