"""Modulo Actividad 7
Se hace fuerte referencia a ayudantia 7"""


class Terreno:
    "Clase Nodo: Terreno"

    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = set()

    def conectar(self, terreno):
        "Agregar un terreno"
        self.conexiones.add(terreno.nombre)

    def desconectar(self, terreno):
        "Eliminar un terreno"
        self.conexiones.remove(terreno.nombre)


class Ciudad:
    "Clase Grafo: Ciudad"

    def __init__(self, path):
        self.dicc_terrenos = dict()
        with open(path, 'r') as file:
            for line in file:
                origen, destinos = line.strip().split(': ')
                lista_destinos = destinos.strip().split(",")
                for destino in lista_destinos:
                    self.agregar_calle(origen, destino)
                    # print(origen, destino)

    def _crear_terreno(self, nombre):
        "Crea un terreno"
        nodo = self.dicc_terrenos.get(nombre)
        if nodo is None:
            nodo = Terreno(nombre)
            self.dicc_terrenos[nombre] = nodo
        return nodo

    def agregar_calle(self, origen, destino):
        "Agregar calle si es que no existe"
        nodo_origen = self._crear_terreno(origen)
        if destino not in nodo_origen.conexiones:
            nodo_destino = self._crear_terreno(destino)
            nodo_origen.conectar(nodo_destino)

    def eliminar_calle(self, origen, destino):
        "Eliminar calle si es que existe"
        nodo_origen = self.dicc_terrenos.get(origen)
        nodo_destino = self.dicc_terrenos.get(destino)
        if nodo_origen is None or nodo_destino is None:
            return ()
        if destino in nodo_origen.conexiones:
            nodo_origen.desconectar(nodo_destino)
            return (origen, destino)
        return ()

    @property
    def terrenos(self):
        "Getter de terrenos"
        keys = set()
        for key in self.dicc_terrenos:
            keys.add(key)
        return keys

    @property
    def calles(self):
        "Getter de calles"
        calle = list()
        for terreno in self.terrenos:
            nodo = self.dicc_terrenos[terreno]
            for vecino in nodo.conexiones:
                calle.append((terreno, vecino))
        return calle

    def verificar_ruta(self, ruta):
        "Verificar existencia de ruta"
        if ruta == []:
            return True
        if len(ruta) == 1:
            if ruta[0] in self.terrenos:
                return True
            return False
        terreno_actual = ruta.pop(0)
        if ruta[0] in self.dicc_terrenos[terreno_actual].conexiones:
            return self.verificar_ruta(ruta)
        return False

    def entregar_ruta(self, origen, destino):
        "Entregar ruta, se usa fuerte referencia con ayudantia 7"
        if origen == destino:
            return True
        origen = self.dicc_terrenos.get(origen)
        destino = self.dicc_terrenos.get(destino)
        if origen is None or destino is None:
            return []
        cola = [[origen]]
        visited = list()
        while cola:
            current_path = cola.pop(0)
            current = current_path[-1]
            if current not in visited:
                lista_vecinos = [self.dicc_terrenos.get(x)
                                 for x in current.conexiones]
                for vecino in lista_vecinos:
                    cola.append(list(current_path) + [vecino])
                    if vecino == destino:
                        return [nodo.nombre for nodo in cola[-1]]
                visited.append(current)
        return []

    def ruta_corta(self, origen, destino):
        "BONUS"
        return self.entregar_ruta(origen, destino)

    def ruta_entre_bombas(self, origen, *destinos):
        "Entrega rutas utilizando funcion anterior y puntos elegidos"
        caminos = list()
        for destino in destinos:
            camino = self.entregar_ruta(origen, destino)
            caminos.append(camino)
            if not camino:
                return []
            origen = camino[-1]
        final = caminos.pop(0)
        for camino in caminos:
            final.extend(camino[1:])
        return final

    def ruta_corta_entre_bombas(self, origen, *destinos):
        "BONUS"
        return self.ruta_entre_bombas(origen, *destinos)


if __name__ == '__main__':
    FACIL = Ciudad("facil.txt")
    MEDIO = Ciudad("medio.txt")
    DIFICIL = Ciudad("dificil.txt")
    NEBIL = Ciudad("kratos.txt")
    print(FACIL.entregar_ruta("A", "E"))
    print(MEDIO.entregar_ruta("A", "E"))
    print(DIFICIL.entregar_ruta("A", "E"))
    print(NEBIL.entregar_ruta("A", "E"))
    # Agrega aqui tus consultas
