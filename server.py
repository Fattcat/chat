import socket

# Vytvorenie serverového socketu
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Nastavenie adresy a portu, na ktorom server počúva
server_address = ('0.0.0.0', 12345)  # Adresa a port môžete zmeniť podľa potreby
server_socket.bind(server_address)

# Server začne počúvať na zadanom porte
server_socket.listen(1)  # Počet klientov, ktorí môžu byť pripojení súčasne

print("Server čaká na pripojenie klienta...")

# Akceptovanie pripojenia od klienta
client_socket, client_address = server_socket.accept()
print(f"Pripojený klient: {client_address}")

while True:
    message = input("Zadajte správu pre klienta: ")
    client_socket.send(message.encode())

    if message.lower() == 'koniec':
        break

client_socket.close()
server_socket.close()
