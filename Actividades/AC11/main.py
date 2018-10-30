"Docstring"
import os


def buscar_archivo(nombre, cwd=os.getcwd()):
    "Docstring"
    for root, _, files in os.walk(cwd):
        if nombre in files:
            aux = os.path.join(root, nombre)
            return aux
    return None


def leer_archivo(path):
    "Docstring"
    aux = list()
    with open(path, "rb") as file:
        bites = file.read()
        for i in range(0, len(bites), 2):
            byte_1, byte_2 = bites[i:i+2]
            real_1 = str(bin(byte_1)[2:].zfill(7))
            real_2 = str(bin(byte_2)[2:].zfill(7))
            final = real_1+real_2
            aux.append(final.lstrip("0")[1:])
        return aux


def decodificar(bits):
    print(bits)


def escribir_archivo(ruta, chunks):
    pass


# Aquí puedes crear todas las funciones extra que requieras.


if __name__ == "__main__":
    nombre_archivo_de_pista = "himno.shrek"
    ruta_archivo_de_pista = buscar_archivo(nombre_archivo_de_pista)

    chunks_corruptos_himno = leer_archivo(ruta_archivo_de_pista)

    chunks_himno = [decodificar(chunk) for chunk in chunks_corruptos_himno]

    nombre_ubicacion_himno = "himno.png"
    escribir_archivo(nombre_ubicacion_himno, chunks_himno)
