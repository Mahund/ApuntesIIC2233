from collections import namedtuple, defaultdict
from statistics import mean
from functools import reduce


# NO MODIFICAR ESTA FUNCION
def foreach(function, iterable):
    for elem in iterable:
        function(elem)


# Named tuples para cada entidad
Ciudad = namedtuple("Ciudad", ["sigla_pais", "nombre"])
Pais = namedtuple("Pais", ["sigla", "nombre"])
Persona = namedtuple("Persona", [
    "nombre", "apellido", "edad", "sexo", "ciudad_residencia",
    "area_de_trabajo", "sueldo"
])

###########################

LIMPIADOR = lambda line: line.rstrip().split(",")


def leer_ciudades(ruta_archivo_ciudades):
    '''
    :param ruta_archivo_ciudades: str
    :return: generador
    '''
    with open(file=ruta_archivo_ciudades, mode='r', encoding="utf-8") as file:
        for linea in file:
            yield Ciudad(*(LIMPIADOR(linea)))


def leer_paises(ruta_archivo_paises):
    '''
    :param ruta_archivo_paises: str
    :return: generador
    '''
    with open(file=ruta_archivo_paises, mode='r', encoding="utf-8") as file:
        for linea in file:
            yield Pais(*(LIMPIADOR(linea)))


def leer_personas(ruta_archivo_personas):
    '''
    :param ruta_archivo_personas: str
    :return: generador
    '''
    with open(file=ruta_archivo_personas, mode='r', encoding="utf-8") as file:
        for linea in file:
            yield Persona(*(LIMPIADOR(linea)))


def sigla_de_pais(nombre_pais, paises):
    '''
    :param nombre_pais: str
    :param paises: iterable de Paises (instancias)
    :return: sigla correspondiente al pais nombre_pais: str
    '''
    return[p.sigla for p in paises if p.nombre == nombre_pais][0]


def ciudades_por_pais(nombre_pais, paises, ciudades):
    '''
    :param nombre_pais: str
    :param paises: iterable de Paises (instancias)
    :param ciudades: iterable de Ciudades (instancias)
    :return: generador
    '''
    sigla = sigla_de_pais(nombre_pais, paises)
    return filter(lambda ciudad: ciudad.sigla_pais == sigla, ciudades)


def personas_por_pais(nombre_pais, paises, ciudades, personas):
    '''
    :param nombre_pais: str
    :param paises: iterable de Paises (instancias)
    :param ciudades: iterable de Ciudades (instancias)
    :param personas: iterable de Personas (instancias)
    :return: generador
    '''
    ciudades_del_pais = ciudades_por_pais(nombre_pais, paises, ciudades)
    nombres_ciudades = [c.nombre for c in ciudades_del_pais]
    return filter(lambda p: p.ciudad_residencia in nombres_ciudades, personas)


def sueldo_promedio(personas):
    '''
    :param personas: iterable de Personas (lista de instancias)
    :return: promedio (int o float)
    '''
    values = [int(p.sueldo) for p in personas]
    return mean(values)


def cant_personas_por_area_de_trabajo(personas):
    '''
    :param personas: iterable de Personas (lista de instancias)
    :return: dict
    '''
    def function(dicct, persona):
        dicct[persona.area_de_trabajo] += 1
        return dicct
    return reduce(function, personas, defaultdict(int))


if __name__ == '__main__':
    RUTA_PAISES = "Paises.txt"
    RUTA_CIUDADES = "Ciudades.txt"
    RUTA_PERSONAS = "Personas.txt"

#
    # print(list(personas_por_pais("Chile", list(leer_paises(RUTA_PAISES)),
    # list(leer_ciudades(RUTA_CIUDADES)), list(leer_personas(RUTA_PERSONAS)))))
#

    # (1) Ciudades en Chile
    ciudades_chile = ciudades_por_pais('Chile', leer_paises(RUTA_PAISES),
                                       leer_ciudades(RUTA_CIUDADES))
    foreach(lambda ciudad: print(ciudad.sigla_pais, ciudad.nombre),
            ciudades_chile)

    # (2) Personas en Chile
    personas_chile = personas_por_pais('Chile', leer_paises(RUTA_PAISES),
                                       leer_ciudades(RUTA_CIUDADES),
                                       leer_personas(RUTA_PERSONAS))
    foreach(lambda p: print(p.nombre, p.ciudad_residencia), personas_chile)

    # (3) Sueldo promedio de personas del mundo
    sueldo_mundo = sueldo_promedio(leer_personas(RUTA_PERSONAS))
    print('Sueldo promedio: ', sueldo_mundo)

    # (4) Cantidad de personas por profesion
    dicc = cant_personas_por_area_de_trabajo(leer_personas(RUTA_PERSONAS))
    foreach(lambda elem: print(f"{elem[0]}: {elem[1]}"), dicc.items())
