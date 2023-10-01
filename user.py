import socket

# Vytvorenie klienta socketu
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Adresa a port servera, ku ktorému sa chcete pripojiť
server_address = ('adresa_servera', 12345)  # Zmeňte na skutočnú adresu a port servera

# Pripojenie k serveru
client_socket.connect(server_address)
print("Pripojený k serveru")

while True:
    received_message = client_socket.recv(1024).decode()
    print(f"Server: {received_message}")

    if received_message.lower() == 'koniec':
        break

    message = input("Zadajte správu pre server: ")
    client_socket.send(message.encode())

client_socket.close()
