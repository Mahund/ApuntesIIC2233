14:07 03-09-2018

## Objetos
_By: Mahund_

#### Definicion:

1. En la vida real: `objetos tangibles`
1. En programacion: `coleccion de datos con comportamientos asociados`

#### OPP *(Object-oriented Programming)* :

- Paradigma de programación: modelan las funcionalidades a través de la interacción entre **objetos**  

- *Objetos* son descritos mediantes *clases*, con sus caracteristicas como **atributos** y sus comportamientos como **metodos**  

- Un *objeto* es una **instancia** de una *clase*

#### Encapsulamiento:  
  
- Caracteristica que permite un *mayor nivel de **abstraccion*** en el modelamiento del problema 
	- *Elementos encapsulados*: Aquellos referentes del funcionamiento interno del objeto 
    >Accedidos solamento por metodos propios de la clase  

#### Interfaz:  

- Es la **fachada** para *proteger* la implementacion de la clase e *interactuar* con otros objetos.  
> El *nivel de detalle* de la interfaz corresponde a la *abstraccion*

#####Creacion de Clases:

- La forma mas basica de crear una clase es: 
```python
class Example(object):
    """docstring for Example"""
    def __init__(self, arg):
        self.arg = arg
    
    def method(self):
        print(f"Hi, my argument is {self.arg}") 
```
> Mediante el comando `help(Clase)` permite ver descripcion de una clase.

##### Encapsulamiento en Python:

- **Todos** los *atributos y metodos* son **publicos** en Python.
- Python permite *sugerir* y *sugerir fuertemente* el encapsulamiento de algun elemento 
```python
class Example(object):
    """docstring for Example"""
    def __init__(self, arg_secret, arg_top_secret):
        self._arg = arg_secret
        self.__arg = arg_top_secret
    
    def method_1(self):
        print(f"Hi, my secret argument is {self._arg}")

    def method_2(self):
        print(f"Hi, my top secret argument is {self.__arg}")
``` 
- Se puede acceder normalmente a elementos con *encapsulamiento sugerido*, pero no a los con **doble sugerencia**
- Para poder acceder a elementos *fuertemente sugeridos* se puede utilizar **name mangling**
```Python
instance = Example("secret", "top_secret")
print(instance._Example__arg)
```  
