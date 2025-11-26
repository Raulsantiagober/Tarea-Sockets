import socket
import threading

def recibir_mensajes(conn):
    while True:
        try:
            datos = conn.recv(1024)
            if not datos:
                break
            print("\nCliente:", datos.decode())
        except:
            break

def main():
    host = "127.0.0.1"
    port = 5000

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, port))
    servidor.listen(1)

    print("Servidor escuchando en", host, port)

    conn, addr = servidor.accept()
    print("Cliente conectado:", addr)

   
    hilo = threading.Thread(target=recibir_mensajes, args=(conn,))
    hilo.daemon = True
    hilo.start()


    while True:
        msg = input("Servidor: ")
        try:
            conn.send(msg.encode())
        except:
            break

    conn.close()
    servidor.close()

if __name__ == "__main__":
    main()
