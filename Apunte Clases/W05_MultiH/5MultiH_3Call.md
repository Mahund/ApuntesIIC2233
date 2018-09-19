17:30 10-09-2018

## Metodo `__call__`
_By: Mahund_

#### Definicion:

- Metodo `__call__` se ejecuta con `instancia()`.

#####Ejemplo:

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estomago = list()

    def __call__(self, comida):
        self.estomago.append(comida)


gato = Animal()
gato("comida_de_gato")
```