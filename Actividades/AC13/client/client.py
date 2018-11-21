"""
client.py -- un simple cliente
"""

import pickle
from socket import socket, SHUT_RDWR

HOST = '127.0.0.1'


class Client:
    """
    Una clase que representa un cliente.
    """

    def __init__(self, port):
        self.host = HOST
        self.port = port
        self.socket = socket()
        self.connected = False

        # Este diccionario tiene los comandos disponibles.
        # Puedes modificarlo para agregar nuevos comandos.
        self.commands = {
            "help": self.help,
            "logout": self.logout,
            "ls": self.ls,
            "upload": self.upload,
            "download": self.download
        }

    def run(self):
        """
        Enciende el cliente que puede conectarse
        para enviar algunos comandos al servidor.
        """

        self.socket.connect((self.host, self.port))
        self.connected = True

        while self.connected:
            command, *args = input('$ ').split()
            function = self.commands.get(command)

            if function is None:
                print(f"El comando '{command}' no existe.")
                print("Escribe 'help' para obtener ayuda.")
            elif command == 'help':
                self.help()
            else:
                self.send(pickle.dumps((command, args)))
                function(*args)

    def send(self, message):
        """
        [MODIFICAR]
        Envía datos binarios al servidor conectado por el socket,
        cumpliendo con el protocolo establecido en el enunciado.
        """

        tamano_mensaje_bytes = len(message).to_bytes(4, byteorder="big")
        self.socket.sendall(tamano_mensaje_bytes + message)

    def receive(self):
        """
        [COMPLETAR]
        Recibe datos binarios del servidor, a través del socket,
        cumpliendo con el protocolo establecido en el enunciado.
        """

        tamano_mensaje_bytes = self.socket.recv(4)
        tamano_mensaje = int.from_bytes(tamano_mensaje_bytes, byteorder="big")

        contenido_mensaje_bytes = bytearray()

        while len(contenido_mensaje_bytes) < tamano_mensaje:
            bytes_que_faltan = tamano_mensaje - len(contenido_mensaje_bytes)
            contenido_mensaje_bytes += self.socket.recv(min(4096,
                                                            bytes_que_faltan))

        return contenido_mensaje_bytes

    def help(self):
        print("Esta es la lista de todos los comandos disponibles.")
        print('\n'.join(f"- {command}" for command in self.commands))

    def ls(self):
        """
        [COMPLETAR]
        Este comando recibe una lista con los archivos del servidor.

        Ejemplo:
        $ ls
        - doggo.jpg
        - server.py
        """

        lista_directorio = pickle.loads(self.receive())
        for elem in lista_directorio:
            print(f"- {elem}")

    def upload(self, *filename):
        """
        [COMPLETAR]
        Este comando envía un archivo hacia el servidor.
        """
        try:
            for name in filename:
                with open(name, "rb") as file:
                    data = file.read()
                self.send(data)
        except:
            print("Error en carga de archivos")

    def download(self, *filename):
        """
        [COMPLETAR]
        Este comando recibe un archivo ubicado en el servidor.
        """
        try:
            for name in filename:
                with open(name, "wb") as file:
                    data = self.receive()
                    file.write(data)
        except:
            print("Error en descarga de archivos")

    def logout(self):
        self.connected = False
        self.socket.shutdown(SHUT_RDWR)
        self.socket.close()
        print("Arrivederci.")


if __name__ == '__main__':
    port_ = input("Escriba el puerto: ")
    client = Client(int(port_))
    client.run()
