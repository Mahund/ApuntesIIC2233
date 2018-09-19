17:30 10-09-2018

## Clase Abstracta
_By: Mahund_

#### Definicion:

- Clases que representan objetos que jamas son instanciados a menos que sea mediante subclases.

- Permiten ahorrar repetir las variables y metodos 

- Poseen:
    - Metodos abstractos: **deben** ser implementados en subclases (overriding)
    - Metodos normales: metodos que se comporta igual en todas las subclases

#### @abstract:

- **@abstractmethod:** Evitan que clases abstractas sean instanciadas o heredadas incompletamente

- **@abstractproperty:** Evitan que clases abstractas sean instanciadas o heredadas incompletamente
> Debe ser importada desde abc

##### Ejemplos:

```python
from abc import ABC ,abstractproperty, abstractmethod

class Base(ABC):
   
    @abstractmethod
    def func_1(self):
        pass

    @abstractproperty
    def value(self):
        return 'Nunca deberíamos llegar aquí'
```
> No permite instancias clase Base, ni heredar sin definir func_1 ni value.