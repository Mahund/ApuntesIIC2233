14:07 03-09-2018

## Properties
_By: Mahund_

#### Encapsulamiento en Python:

- La manera que tiene Python de *proveer encapsulamiento* es mediante el uso de un mecanismo llamado **properties**.

#### ¿Que son?:

- Funciona como un atributo, pero que modifica su funcionamiento segun su uso:
    1. Al ser leido: `getter`
    1. Al ser escrito: `setter`
    1. Al ser eliminado: `deleter`
    > Permiten ejecutar acciones *limpiamente* (facil de **leer y mantener**)

#### Ejemplo:  
  
1. Property como decorador:
```Python
class Puente:
    
    def __init__(self, maximo):
        self.maximo = maximo
        self.__personas = 0
        
    @property # decorador property genera una funcion getter 
    def personas(self):
        return self.__personas

    @personas.setter #ocupamos la funcion getter.setter para definir una funcion setter
    def personas(self, p):
        if p > self.maximo:
            self.__personas = self.maximo
        elif p < 0:
            self.__personas = 0
        else:
            self.__personas = p
``` 
> Permite tanto el encapsulamiento del atributo *_ _personas*, como una sintaxis amigable con la property *personas*

1. Property explicita:
```Python
class Puente:
    
    def __init__(self, maximo):
        self.maximo = maximo
        self.__personas = 0
        
    def _get_personas(self):
        return self.__personas

    def _set_personas(self, p):
        if p > self.maximo:
            self.__personas = self.maximo
        elif p < 0:
            self.__personas = 0
        else:
            self.__personas = p
        
    personas = property(_get_personas, _set_personas)
``` 
> Permite definir la property ingresando metodos `getter` y `setter` respectivamente

- Ambas formas de property permitiran trabajar utilizando:

```python
puente = Puente(10)
puente.personas += 7
print(f"Hay {puente.personas} personas en el puente.")
puente.personas += 5
print(f"Hay {puente.personas} personas en el puente.")
puente.personas -= 15
print(f"Hay {puente.personas} personas en el puente.")
```