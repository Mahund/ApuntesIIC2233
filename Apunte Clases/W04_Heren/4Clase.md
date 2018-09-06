14:07 06-09-2018

## OOP
_By: Mahund_

#### Introduccion:

```python
class Paya:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def _to_bits(self):
        return (self.lyrics.lower()
            .replace("cero", "0")
            .replace("uno", "1")
            .replace("\n", "")
            .replace(" ", "")
            .replace(",", ""))

    def to_text(self):
        b = self._to_bits()
        return int(b, 2).to_bytes(len(b) //8, "big").decode()
```

#### Objetos:

- Es un **paradigma** (forma de programacion) en el cual se *modelan* los objetos del mundo real en el codigo

- Permite una mejor **lectura** y **mantenimiento** del codigo

#### Encapsulamiento:

- Propiedades que busco que el objeto tenga

- **Properties:** ayudan para encapsular atributos y no accederlos de forma directa
> Para que el usuario no acceda a todo, para evitar enredarlo
> Funcion que recibe getter, setter, deleter, con uso de decorador

##### Usos de Property:

1. Ayuda para **validar** inputs
1. Obtener calculos como atributos (edad, tiempo_usado, etc)

#### Interfaz:

- Lo que es accesible desde fuera del codigo por el usuario

##### Atributos de Clase:

- Relacion con los metodos estáticos: metodo compartido con todas las clases, pero que no sacan informacion dependiendo de la instancia (de uso comun)

##### Atributos y Metodos de Instancia:

- Atributos de instancia se ven en `__init__`

##### Composicion vs Agregacion:

- **Composicion:** relacion fuerte (rombo oscurecido)

- **Agregacion:** relacion debil (rombo vacio)

- **Herencia:** comparten elementos pero con cosas nuevas o editadas con **overriding**

##### Duck typing:

- No ocupa herencia, solo comparten nombre de metodos
