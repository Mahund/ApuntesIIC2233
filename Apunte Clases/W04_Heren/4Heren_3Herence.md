14:07 03-09-2018

## Herencia
_By: Mahund_

#### Definicion:

- Relacion de *especializacion* y *generalizacion* entre objetos

- *Subclase* **hereda** atributos y metodos de una *Superclase*

- Subclase posee *mismas caracteristicas* ademas de sus **propias**

> Objeto *b* es un objeto *a* con ciertas diferencias

#### Ejemplo:  
  
- Furgon hereda desde Auto:
```Python
class Auto:
    """Superclase de FurgonEscolar"""
    
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        
    def conducir(self, distancia):
        print(f"Conduciendo {distancia} kilómetros")
        
    def realizar_mantencion(self):
        print("Realizando mantención")

class FurgonEscolar(Auto):
    """Subclase de Auto"""
    
    # Estamos haciendo overriding del __init__ original
    def __init__(self, marca, modelo, motor):
        # Usamos el __init__ original para setear los otros datos. Así es como podemos llamarlo con super().
        super().__init__(marca, modelo, motor)
        self.ninos = []
    
    # inscribir_nino es un método específico de esta subclase.
    def inscribir_nino(self, nino):
        self.ninos.append(nino)
        
    # Estamos haciendo overriding del método conducir original
    def conducir(self, distancia):
        # Acá no queremos usar la versión original de conducir
        print(f"Conduciendo con cuidado {distancia} kilómetros")
``` 
> `Overriding`: permite sobreescribir sobreescribir metodos de superclase con el mismo nombre pero algoritmos diferentes.  
> `super`: permite utilizar la implementacion de un metodo de la superclase

#### Herencia y built-ins:

- Podemos ocupar como *superclase* un build-in, y utilizando *override* podemos personalizarlo agregando/editando metodos propios.