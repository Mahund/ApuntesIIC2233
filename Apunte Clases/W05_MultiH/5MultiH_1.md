17:30 10-09-2018

## Multiherencia
_By: Mahund_

#### Definicion:

- Python permite heredar de más de una sola *superclase*

##### Ejemplo :

```python
class Ejemplo(super1, super2):
    """docstring for Ejemplo"""
    super1.__init__()
    super2.__init__()
    def __init__(self, arg):
        self.arg = arg
        
```
> Hereda atributos y metodos desde superclases 1 y 2.

#### Problema del diamante:  
  
- En ejemplo anterior se llama metodo `__init__` de ambas superclases, lo que genera que clase **object** (que todas las clases heredan por default) sea llamada 2 veces en vez de 1.

- **Llamar directamente** con **n** numero de *superclases* genera un **n** llamados en *object*.

- Esto se soluciona mediante `super()`

##### Super():  

- Permite el llamado correcto de *superclases* cuando se realiza **multiherencia**

- Genera un **orden de llamado** relacionado con el orden de la multiherencia.

```python
class Ejemplo(super1, super2):
    """docstring for Ejemplo"""
    super().init()
    def __init__(self, arg):
        self.arg = arg
        
```

##### Metodo `__mro__`:

- Metodo que permite visualizar el **orden de herencia** en una clase.
> Method resolution orden utiliza algoritmo **C3**

```python
ejemplo = Ejemplo(arg)
ejemplo.__mro__
```

#### Multiherencias inviables:

- Existen varias estructuras de herencias inconsistentes:

```python
class X:
    pass
class Y:
    pass
class A(X, Y):
    pass
class B(Y, X):
    pass
class F(A, B):
    pass
```
> Existencia de clase F genera una estructura inviable de herencia. Se corrige eliminando F o cambiando orden de herencia en A o B.

#### Args `*args` y Keyword-args `**kwargs`:

- Permiten entregar correctamente los parametros segun una llave (key) en multiherencia
    1. Args: mediante `*` empaqueta/desempaqueta parametros segun su orden
    1. Kwargs: midiante `**` empaqueta/desempaqueta parametros segun su llave.

```python
def func(a, b, c):
    print(c)

values = [1, 2, 3]
func(*values)

kwvalues = {"a": 1, "c": 3, "b":2}
func(**kwvalues)
```
> Ambos imprimen correctamente 3.

```python
def func(*args):
    for arg in args:
        print(arg)

func(1,2)
func(1,2,3)
```
> Funcion que recibe indefinidos parametros

#### Ejemplo Mixto:

```python
class Investigador:
    def __init__(self, area="", **kwargs):
        print(f"init Investigador con area {area} y kwargs:{kwargs}")
        super().__init__(**kwargs)
        self.area = area
        self.num_publicaciones = 0
        
class Docente:
    def __init__(self, departamento="", **kwargs):
        print(f"init Docente con depto {departamento} y kwargs:{kwargs}")
        super().__init__(**kwargs)
        self.departamento = departamento
        self.num_cursos = 3
        
class Academico(Docente, Investigador):
    def __init__(self, nombre, oficina, **kwargs):
        print(f"init Academico con nombre {nombre}, oficina {oficina}, kwargs:{kwargs}")
        super().__init__(**kwargs)
        self.nombre = nombre
        self.oficina = oficina

print(Academico.__mro__)
p1 = Academico("Emilia Donoso", oficina="O5", area="Inteligencia de Máquina", departamento="Ciencia De La Computación")
print("--------")
print(p1.nombre)
print(p1.area)
print(p1.departamento)
```