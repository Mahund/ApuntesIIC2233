"Modulo para Actividad12"
import json
import pickle
from datetime import datetime
from time import sleep
from hashlib import blake2b

RECETAS_LOCK_PATH = 'RecetasLockJSON.json'
INGREDIENTES_PATH = 'ingredientes.txt'
'''
=====================================
NO BORRAR NI CAMBIAR!
'''
SUPER_SECRET_KEY = b'IIC2233'
'''
=====================================
'''


class Receta:
    """Clase que modela una receta del 'PyKitchen' cookbook"""

    def __init__(self, nombre='', ingredientes=None, alinos=None):
        self.nombre = nombre
        self.ingredientes = ingredientes or []
        self.alinos = alinos or []
        self.llave_segura = None

    @property
    def verificada(self):
        """Property que nos indica si una receta fue limpiada o no."""
        return hasattr(
            self, 'llave_segura') and self.llave_segura == self.encriptar()

    def encriptar(self):
        """Funcion que encripta el valor a partir de una llave secreta"""
        encriptador = blake2b(key=SUPER_SECRET_KEY, digest_size=16)
        encriptador.update(self.nombre.encode())

        return encriptador.hexdigest()

    @staticmethod
    def abrir_ingredientes():
        """Genera las líneas del archivo ingredientes.txt"""
        with open(INGREDIENTES_PATH, encoding='utf-8') as fp:
            yield from map(lambda x: x.strip(), fp)

    def abrir_recetas_lock(self):
        """
        Funcion para abrir el archivo que indica los atributos
        de las recetas
        """
        with open(RECETAS_LOCK_PATH, encoding="utf-8") as file:
            data = json.load(file)
        return set(data)

    def __setstate__(self, state):
        """
        Deserializa

        Elimina los atributos incorrectos y los ingredientes inválidos.
        """
        valid_atributes = self.abrir_recetas_lock()
        valid_ingredients = list(self.abrir_ingredientes())
        atributos_invalidos = list()
        ingredientes_invalidos = list()

        for key in state:
            if key not in valid_atributes:
                atributos_invalidos.append(key)

        for atributo_invalidos in atributos_invalidos:
            state.pop(atributo_invalidos)  # Aca se eliminaron atributos

        for ingrediente in state["ingredientes"]:
            if ingrediente not in valid_ingredients:
                ingredientes_invalidos.append(ingrediente)

        for ingredientes_invalido in ingredientes_invalidos:
            state["ingredientes"].remove(ingredientes_invalido)

        self.__dict__ = state

    def __getstate__(self):
        """
        Serializa

        Recuerda colocar el atributo llave_segura.
        """
        nueva = self.__dict__.copy()
        nueva.update({"llave_segura": self.encriptar()})
        return nueva

    def __repr__(self):
        return str(self.nombre)


class Comida:

    def __init__(self,
                 nombre='',
                 nivel_preparacion=0.0,
                 ingredientes=None,
                 alinos=None,
                 fecha_ingreso=None):
        self.nombre = nombre
        self.nivel_preparacion = nivel_preparacion
        self.ingredientes = ingredientes or []
        self.alinos = alinos or []
        if fecha_ingreso:
            time_delta = datetime.now() - Comida.str_a_date(fecha_ingreso)
            minutos = time_delta.seconds//60
            self.nivel_preparacion += minutos

        ''' Recuerda cambiar aqui el nivel de preparacion de acuerdo a la fecha
        de ingreso!'''

    def __repr__(self):
        return str(self.nombre)

    @property
    def quemado(self):
        return self.nivel_preparacion > 100

    @property
    def preparado(self):
        return self.nivel_preparacion >= 100

    @staticmethod
    def date_a_str(fecha):
        return fecha.strftime('%Y-%m-%d-%H-%M-%S')

    @staticmethod
    def str_a_date(fecha_str):
        return datetime.strptime(fecha_str, '%Y-%m-%d-%H-%M-%S')

    @classmethod
    def de_receta(cls, receta):
        return cls(receta.nombre, 0.0, receta.ingredientes, receta.alinos)


class ComidaEncoder(json.JSONEncoder):
    """Utiliza esta clase para codificar en json"""
    def default(self, obj):

        if isinstance(obj, Comida):
            # print(obj .date_a_str(datetime.now()))
            return {'nombre': obj.nombre,
                    'nivel_preparacion': obj.nivel_preparacion,
                    'ingredientes': obj.ingredientes,
                    'alinos': obj.alinos,
                    'fecha_ingreso': Comida.date_a_str(datetime.now())}

        # Mantenemos la serialización por defecto para otros tipos
        return super().default(obj)


if __name__ == "__main__":
    a = Receta(ingredientes=["caca", "leche"])
    b = pickle.dumps(a)
    c = pickle.loads(b)
    d = Comida("lol")
    print(d)
    e = json.dumps(obj=d, cls=ComidaEncoder)
    sleep(1)

    def json_dencoder(dicto):
        return Comida(**{llave: dicto[llave] for llave in dicto})

    def cargar_personas(x):
        return json.loads(x, object_hook=json_dencoder)
    print("s")
    f = cargar_personas(e)
    print(f.nivel_preparacion)
