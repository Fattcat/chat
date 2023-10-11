import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('adresa_servera', 12345)  # Zmeňte na skutočnú adresu a port servera
    client_socket.connect(server_address)

    # Pripojenie k serveru
    user_name = input("Zadajte svoje meno: ")
    client_socket.send(user_name.encode())

    while True:
        recipient_name = input("Zadajte meno príjemcu: ")
        message = input("Napíšte správu: ")

        client_socket.send(recipient_name.encode())
        client_socket.send(message.encode())

if __name__ == "__main__":
    main()
