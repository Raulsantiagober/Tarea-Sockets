import socket
import threading

def recibir_mensajes(sock):
    while True:
        try:
            datos = sock.recv(1024)
            if not datos:
                break
            print("\nServidor:", datos.decode())
        except:
            break

def main():
    host = "127.0.0.1"
    port = 5000

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, port))

    print("Conectado al servidor.")

    # Hilo para recibir mensajes
    hilo = threading.Thread(target=recibir_mensajes, args=(cliente,))
    hilo.daemon = True
    hilo.start()

    # Bucle para enviar
    while True:
        msg = input("Yo: ")
        try:
            cliente.send(msg.encode())
        except:
            break

    cliente.close()

if __name__ == "__main__":
    main()
