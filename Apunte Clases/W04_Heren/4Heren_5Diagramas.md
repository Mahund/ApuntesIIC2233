14:07 03-09-2018

## Diagrama de Clase
_By: Mahund_

#### Definicion:

- Permite *visualizar* las **clases** (con sus atributos y metodos) que componen un sistema y sus **interacciones**.

#### Clases:  
  
- Estructura que *encapsula la informacion*
> Partir con las clases mas simples hacia las mas complejas
- Representacion visual:

    |Nombre Clase|
    |:----------:|
    |Atributos   |
    |Metodos     | 

#### Relaciones:

1. *Composicion:* la existencia de los objetos *incluidos* **depende** de aquel que los incluye.
> Representada como **rombo relleno** desde clase que agrupa, hacia sus componentes
    - Ej: Los personajes de un juego, si no existe el juego no existirian los personajes (hablando del codigo).

1. *Agregacion:* la existencia de los objetos *incluidos* **es independiente** de aquel que los incluye.
> Representada como **rombo vacio** desde clase que agrupa, hacia sus agregaciones
    - Ej: Los miembro de un escuadron, si no existe el escuadron los miembros siguen existiendo.

1. *Herencia:* **subclase** *hereda* atributos y metodos de una **superclase**, agregando **elementos propios** de la subclase.
> Representada como **flecha vacia** que apunta a superclase desde subclases
    - Ej: Clases Camionetas y Camiones que heredan desde clase Vehiculo.

#### Modelo integrado:

- Representacion de *todas las clases* con sus correspondientes relaciones mencionadas.