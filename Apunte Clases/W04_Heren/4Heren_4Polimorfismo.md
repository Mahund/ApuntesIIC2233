14:07 03-09-2018

## Polimorfismo
_By: Mahund_

#### Definicion:

- Es la posibilidad de enviar mensajes sintacticamente iguales a distintos objetos de distintas clases.

#### Tipos:  
  
1. *Overriding*: ocurre al implementar en subclase un metodo de *igual nombre* de su superclase, **invalidando** este ultimo.  

1. *Overloading*: Python **no** lo implementa, pero permite crear metodos de igual nombre pero distinto numero/tipo de argumentos.  
> Puede simularse con argumentos por defecto o numero variable de argumentos

##### Overloading en operadores:

- *Suma (+):*
```python
from collections import namedtuple


Productos = namedtuple('Productos', ['pan', 'leche', 'agua'])

class Carro(Productos):
    '''
    Un carro de compras lo representaremos como un namedtuple
    '''
    
    def __add__(self, otro):
        # Nota: Esto se puede escribir mucho más elegante con los contenidos de programación funcional
        valores = tuple(self)
        valores_otro = tuple(otro)
        valores_sumados = []
        
        for i in range(len(self)):
            valores_sumados.append(valores[i] + valores_otro[i])
            
        return Carro(*valores_sumados)
```
> Implementacion similar para el resto: `__lt__`, `__eq__`, `__str__`, `__repr__`. (Sobrecargas)

#### Duck typing:

- No importa el tipo de objeto si la accion existe

- Objetos de clase distinta, pero con metodos de igual nombre pueden llamarse igualmente

```python
class Pato:
    
    def gritar(self):
        print("Quack!")
        
    def caminar(self):
        print("Caminando como un pato")        
    
class Persona:
    
    def gritar(self):
        print("Ahhh!")
        
    def caminar(self):
        print("Caminando como un humano")        

        
def activar(pato): # Esto en otro tipo de lenguaje obligaría a que pato sea del tipo "Pato", por lo tanto
    pato.gritar() # la función activar no podría ser llamada con un argumento tipo "Persona"
    pato.caminar()

donald = Pato()
juan = Persona()
activar(donald)
activar(juan)
```