"Actividad 9"
import threading
from time import sleep as tutito
from itertools import chain
from random import randint, random


def desencriptar(nombre_archivo):
    """
    Esta simple (pero útil) función te permite descifrar un archivo encriptado.
    Dado el path de un archivo, devuelve un string del contenido desencriptado.
    """

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        murcielago, numeros = "murcielago", "0123456789"
        dic = dict(chain(zip(murcielago, numeros), zip(numeros, murcielago)))
        return "".join(
            dic.get(char, char) for linea in archivo for char in linea.lower())


class Equipo(threading.Thread):
    "Equipo"
    def __init__(self, nombre, evento, nebil):
        super().__init__()
        self.nombre = nombre
        self.hacker = Hacker(nombre)
        self.cracker = Cracker(nombre, nebil)
        self.termino = evento
        self.daemon = True
        self.gano = False

    def run(self):
        "Run"
        self.hacker.start()
        self.cracker.start()
        self.hacker.join()
        self.cracker.join()
        self.termino.set()
        self.gano = True

    def __repr__(self):
        return f"{self.nombre}, Cracker escribio {self.cracker.lineas}\
 lineas y hacker {'si' if self.hacker.logro_hackear else 'no '}\
 logro hackear el sistema"


class Hacker(threading.Thread):
    "Hacker se encarga de desencriptar"
    def __init__(self, team_name):
        super().__init__()
        self.daemon = True
        self.team = team_name
        self.logro_hackear = False

    def run(self):
        tutito(randint(4, 12))
        string = desencriptar("pista.txt")
        with open(f"pista_{self.team}.txt", "w", encoding="UTF-8") as file:
            file.write(string)
        print(f"Hacker de {self.team} termino ")
        self.logro_hackear = True

    def __repr__(self):
        return f"Hacker"


class Cracker(threading.Thread):
    "Cracker creara una inyeccion"
    def __init__(self, team_name, nebil):
        super().__init__()
        self.daemon = True
        self.team = team_name
        self.lineas = 0
        self.nebil = nebil
        # print(Mision.algo)  # Es solo para ver como acceder a var de clase

    def run(self):
        while self.lineas < 50:
            self.lineas += randint(5, 15)
            tutito(1)
            if random() < 0.2:
                with self.nebil:
                    print(f"NebilLockbottom empezo reparacion \
con {self.team}")
                    tutito(randint(1, 3))
                    print(f"NebilLockbottom termino  reparacion \
con {self.team}")
        print(f"Cracker de {self.team} termino ")

    def __repr__(self):
        return f"Cracker"


class Mision(threading.Thread):
    "Mision"
    algo = True

    def __init__(self):
        super().__init__()
        self.termino = threading.Event()
        self.nebil = threading.Lock()
        self.equipos = [Equipo(f"Equipo {i+1}", self.termino, self.nebil)
                        for i in range(3)]

    def run(self):
        for equipo in self.equipos:
            equipo.start()
        self.termino.wait()


if __name__ == "__main__":
    MISION = Mision()
    MISION.start()
    MISION.join()
    WINNER = None
    for team in MISION.equipos:
        print(team)
        if team.gano:
            WINNER = team
    print(f"El ganador es {WINNER.nombre}")
