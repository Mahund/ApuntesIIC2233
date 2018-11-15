19:43 05-11-2018

## Serializacion
_By: Mahund_

#### Introduccion:

- Método para poder almacenar información no lineal en forma de bytes.

#### Pickle:

- Esta libreria permite guardar y cargar casi cualquier objeto en python.

- Guardar: `dumps` (Serializar)
- Cargar: `loads` (Deserializar)

```python
import pickle

tupla = ("a", 1, 3, "hola")
serializacion = pickle.dumps(tupla)

print(serializacion)
print(type(serializacion))
print(pickle.loads(serializacion))import pickle
```

Pickle permite lo anterior mediante archivos:
```python
lista = [1, 2, 3, 7, 8, 3]

with open("mi_lista.bin", 'wb') as file:
    pickle.dump(lista, file)

with open("mi_lista.bin", 'rb') as file:
    lista_cargada = pickle.load(file)

print(f"¿Las listas son iguales? {lista == lista_cargada}")
print(f"¿Las listas son el mismo objeto? {lista is lista_cargada}")
```
> Pickle es **MUY PEIGROSO**, asi que deben conocerse los archivos a abrir.

#### Personalizar Serializacion

- Para serializar pickle revisa `__getstate__`, el cual debe retornar diccionario con atributos a serializar. Si no esta implementado entonces se utilizara `__dict__`.


#### Personalizar Deserializacion

- Para deserializar pickle revisa `__setstate__`, el cual se ejecuta cada vez que se llama al metodo `load` o `loads`. Recibe como argumento el diccionario que representa al *objeto serializado* , para luego asignarlo al diccionario del objeto `self.__dict__ = diccionario_serializado`. Si no esta implementado entonces se utilizara `__dict__`.


##### Ejemplo

```python
import pickle
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.mensaje = "No pasa nada"
        
    def __getstate__(self):
        nueva = self.__dict__.copy()
        nueva.update({"mensaje": "¡Me están serializando!"})
        # esto es lo que será serializado por pickle
        return nueva 

    def __setstate__(self, state):
        print("Objeto recién deserializado, actualizando su estado")
        state.update({"nombre": state["nombre"] + " deserializado"})
        self.__dict__ = state
original = Persona("Juan", 30)

print("Nombre original:", original.nombre)
serializado = pickle.dumps(original)

deserializado = pickle.loads(serializado)
print("Nombre deserializado:", deserializado.nombre)
```

#### Serializar con JSON

- Desventaja de `pickle`: solo puede ser deserializado con `python`

- Solucion: **JSON:** formato estandar de intercambio de datos utilizable por multiples lenguajes. El formato en que almacena la informacion es **similar a diccionarios** de python.

- Objetos serializables: `int`, `str`, `float`, `dict`, `bool`, `list`, `tuple` y `NoneType`.

- Libreria `json`en python posee igualmente metodos dumps y loads.
```python
from itertools import count
import json

class Persona:
    id = count()
    
    def __init__(self, nombre, edad, estado_civil):
        self.nombre = nombre
        self.edad = edad
        self.estado_civil = estado_civil
        self.id_ = next(self.id)

p = Persona("Juan", 35, "Soltero")

json_string = json.dumps(p.__dict__)
print("Datos en formato JSON:", type(json_string), json_string)

json_deserializado = json.loads(json_string)
print("Datos en formato Python:", type(json_deserializado), json_deserializado)
```

#### Personalizar Serializacion JSON

- 