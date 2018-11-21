import json
import os
import pickle

from clases import Comida, ComidaEncoder

BOOK_PATH = 'recetas.book'


class PyKitchen:
    def __init__(self):
        self.recetas = []
        self.comidas = []
        self.despachadas = []

    def cargar_recetas(self):
        '''Esta función se encarga de cargar el archivo recetas.book'''
        with open(BOOK_PATH, 'rb') as file:
            lista_cargada = pickle.load(file)
            for receta in lista_cargada:
                self.recetas.append(receta)
        print("Cargar", len(self.recetas))

    def guardar_recetas(self):
        '''Esta función se encarga de guardar las recetas (instancias), en el
        archivo recetas.book'''
        with open(BOOK_PATH, 'wb') as file:
            pickle.dump(self.recetas, file)
        print("Guardar")

    def cocinar(self):
        '''Esta funcion debe:
        - filtrar recetas verificadas
        - crear comidas a partir de estas recetas
        - guardar las comidas en la carpeta horno
        '''
        for receta in self.recetas:
            if receta.verificada:
                comida = Comida.de_receta(receta)
                with open(f"horno/{receta.nombre}.json", "w", encoding="utf-8") as file:
                    json.dump(comida, file, cls=ComidaEncoder)

    def despachar_y_botar(self):
        ''' Esta funcion debe:
        - Cargar las comidas que están en la carpeta horno.
            Pro tip: string.endswith('.json') retorna true si un string
            termina con .json
        - Crear instancias de Comida a partir de estas.
        - Guardar en despachadas las que están preparadas
        - Imprimir las comidas que están quemadas
        - Guardar en comidas las no preparadas ni quemadas
        '''
        paths = list(filter(lambda p: p.endswith('.json'), os.listdir("horno")))
        for path in paths:
            real = os.path.join("horno", path)
            with open(real, encoding="utf-8") as file:
                comida = json.load(file, object_hook=lambda x: Comida(**x))
                if comida.quemado:
                    print(comida.nombre)
                elif comida.preparado:
                    self.despachadas.append(comida)
                else:
                    self.comidas.append(comida)
        # No me alcanzo el tiempo


if __name__ == "__main__":
    a = PyKitchen()
    a.cargar_recetas()
    a.cocinar()
    a.despachar_y_botar()
