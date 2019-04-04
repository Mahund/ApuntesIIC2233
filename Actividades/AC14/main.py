import json
import re
from time import sleep
import os

import requests

from credenciales import API_KEY


API_URL = "https://api.nasa.gov/planetary/apod"
DIR_IMAGENES = 'imagenes'
PATH_RESULTADOS = 'resultados.txt'


def limpiar_fecha(linea):
    '''
    Esta función se encarga de limpiar el texto introducido a las fechas

    :param linea: str
    :return: str
    '''
    linea = linea.strip("\n")  # Esto es solo por el salto de linea del archivo
    return re.sub('</?[a-zA-Z0-9]+>', '', linea)


def chequear_fecha(fecha):
    '''
    Esta función debe chequear si la fecha cumple el formato especificado

    :param fecha: str
    :return: bool
    '''
    pattern = "([0-9]{4}-)?[0-9]{2}-[0-9]{2}"
    return bool(re.fullmatch(pattern, fecha))


def obtener_fechas(path):
    '''
    Esta función procesa las fechas para devolver aquellas que son útiles
    para realizar las consultas a la API

    :param path: str
    :return: iterable
    '''
    with open(path) as file:
        for linea in file:
            candidato = limpiar_fecha(linea)
            if chequear_fecha(candidato):
                yield candidato


def obtener_info(fecha):
    '''
    Recibe una fecha y retorna un diccionario
    con el título, la fecha y el url de la imagen
    :param fecha: str
    :return: dict
    '''
    info = requests.get(API_URL, params={'api_key': API_KEY, 'date': fecha})
    data = info.json()
    return {"titulo": data["title"],
            "fecha": data["date"],
            "URL": data["url"]}


def escribir_respuesta(datos):
    '''
    Esta función debe escribir las respuestas de la API en el archivo
    resultados.txt

    :param datos_respuesta: dict
    '''
    with open(PATH_RESULTADOS, "a") as file:
        fecha = datos["fecha"]
        titulo = datos["titulo"]
        url = datos["URL"]
        file.write(f"{fecha} --> {titulo}: {url}\n")
        name = url.split("/")[-1]
        path = os.path.join("imagenes", name)
        print(f"Se agrega archivo {name}")
        descargar_imagen(url, path)


def descargar_imagen(url, path):
    '''
    Recibe la url de una imagen y guarda los datos en un archivo en path

    :param url: str
    :param path: str
    '''
    respuesta = requests.get(url, stream=True)
    if respuesta.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in respuesta:
                f.write(chunk)


if __name__ == "__main__":
    PATH_FECHAS = 'fechas_secretas.txt'
    with open(PATH_RESULTADOS, "w"):
        pass  # Esto es solo para que este vacio el archivo con resultados

    for fecha in obtener_fechas(PATH_FECHAS):
        respuesta = obtener_info(fecha)
        escribir_respuesta(respuesta)
