27-09-2018

## Grafos
_By: Mahund_

#### Introduccion:

- No lo haga:
    1. Asignar a `built-in`:
    ```python
    set = {1, 2, 3}
    ```
    1. Importar todo:
    ```python
    from module import *
    ```
    1. Igualar `None`:
    ```python
    if ejemplo == None:
    ```
    1. Ocupar `type` para ver clase en vez de `isinstance` que revisa lo heredado
    1. Recorrer `dict.keys()` en vez de recorrer el diccionario directamente
    1. Parametros mutables por default, ya que el valor default va a variar para siempre con cada llamada
    ```python
    def func(param=[]):
        param.append("Hola")
        return param
    ```

#### Grafo:

- Se puede representar con:
    1. Nodos
    1. Lista Adyacencia
    1. Matriz Adyacencia
    1. Matriz Incidencia

- Se pueden recorrer:
    1. Con BFS se garantiza que se vea el camino más corto