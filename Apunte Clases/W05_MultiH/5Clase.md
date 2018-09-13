13-09-2018

## OOP2
_By: Mahund_

#### Introduccion:

- Desempaquetar elementos: 
```python
product_info = ("name", "lastname", "value", "numer")
name_var, lastnime_var, *others = product_info
```

- Tambien puede omitirse el nombre others:
```python
name_var, *_ = product_info
```

#### Herencia Multiple:

- Permite heredar de multiples

- Ocupa metodo super() para evitar problema del diamante

#### Clases Abstractas:

- Clases creadas para nunca ser instanciadas

- Se puede evitar importando de abc: ABC, abstractmethod, abstracproperty

#### Overloading:

- Permite definir funciones con distinto tipo y/o numero de parametros

- No esta implementado en python

- Se puede "imitar" mediante `*args`

#### Metodo `__call__`:

- Se pueden volver *llamables* las clases

#### Metodo estatico:

- No necesitan de self, ya que son independientes de la instancia (no acceden a valores propios)