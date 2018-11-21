"""
server.py -- un simple servidor
"""

import pickle
from socket import socket
import os

HOST = '127.0.0.1'


class Server:
    """
    Una clase que representa un servidor.
    """

    def __init__(self, port):
        self.host = HOST
        self.port = port
        self.client = None
        self.socket = socket()

        self.commands = {
            "ls": self.list_filenames,
            "download": self.send_file,
            "upload": self.save_file,
            "logout": self.disconnect,
        }

    def run(self):
        """
        Enciende el servidor que puede conectarse
        y recibir comandos desde un único cliente.
        """

        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        print(f"Escuchando en {self.host}:{self.port}.")

        while self.client is None:
            self.client, _ = self.socket.accept()
            print("¡Un cliente se ha conectado!")

            while self.client:
                command, args = pickle.loads(self.receive())
                self.commands[command](*args)

        print("Arrivederci.")

    def send(self, message):
        """
        [COMPLETAR]
        Envía datos binarios al cliente conectado por el socket,
        cumpliendo con el protocolo establecido en el enunciado.
        """

        tamano_mensaje_bytes = len(message).to_bytes(4, byteorder="big")
        self.client.sendall(tamano_mensaje_bytes + message)

    def receive(self):
        """
        [MODIFICAR]
        Recibe datos binarios del cliente, a través del socket,
        cumpliendo con el protocolo establecido en el enunciado.
        """

        tamano_mensaje_bytes = self.client.recv(4)
        tamano_mensaje = int.from_bytes(tamano_mensaje_bytes, byteorder="big")

        contenido_mensaje_bytes = bytearray()

        while len(contenido_mensaje_bytes) < tamano_mensaje:
            bytes_que_faltan = tamano_mensaje - len(contenido_mensaje_bytes)
            contenido_mensaje_bytes += self.client.recv(min(4096,
                                                            bytes_que_faltan))

        return contenido_mensaje_bytes

    def list_filenames(self):
        """
        [COMPLETAR]
        Envía al cliente una lista que contiene los nombres de
        todos los archivos existentes en la carpeta del servidor.
        """

        self.send(pickle.dumps(os.listdir()))

    def send_file(self, *filename):
        """
        [COMPLETAR]
        Envía al cliente un archivo ubicado en el directorio del servidor.
        """
        try:
            for name in filename:
                with open(name, "rb") as file:
                    data = file.read()
                self.send(data)
        except:
            print("Error en envio de archivos")

    def save_file(self, *filename):
        """
        [COMPLETAR]
        Guarda un archivo recibido desde el cliente.
        """
        try:
            for name in filename:
                with open(name, "wb") as file:
                    data = self.receive()
                    file.write(data)
        except:
            print("Error en guardado de archivos")

    def disconnect(self):
        self.client = None
        print("El cliente se ha desconectado.")


if __name__ == '__main__':
    port_ = input("Escriba el puerto: ")
    server = Server(int(port_))
    server.run()
