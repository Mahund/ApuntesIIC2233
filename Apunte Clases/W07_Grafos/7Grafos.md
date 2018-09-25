15:30 24-09-2018

## Grafos
_By: Mahund_

#### Definiciones:

- Conjunto **no vacio** de *nodos* y las *relaciones* entre estos.

- Cada *nodo* es llamado **vertice** y cada *relacion* es llamada **arista**.

- Puede ser **dirigidos** o **no dirigidos**: existencia o no de *orientacion en las aristas*.
> Dirigido: A esta relacionado con B pero no necesariamente B lo este con A.

#### Estructuras:

1. Representacion con Nodos
    - Clase mas *natural*, funciona tal como los arboles
    - Cada vertice posee lista de vertices relacionados
    ```python
    class Node:
    
    def __init__(self, value):
        self.value = value
        self.connections = []
        
    def add_vertex(self, value):
        self.connections.append(value)
        
    def __repr__(self):
        r = f"[{self.value}]"
        if self.connections:
            r += " -> (" + ", ".join([repr(c) for c in self.connections]) + ")"
        return r 
    ```

1. Listas de Adyacencia
    - Todos los vertices son almacenados en una lista
    - Cada vertice posee lista de vertices relacionados
    ```python
    # Aquí usamos diccionarios "int-list" porque ofrece más facilidad de búsqueda.
    # También podrían ser list(tuple(int, list)). ¿Por qué no sería correcto hacer list(list(int, list))?

    grafo_no_dirigido = {1: [2], 2: [1, 3], 3: [2, 4, 5], 4: [3, 5], 5: [3, 4]}
    grafo_dirigido = {1: [2], 2: [3], 3: [4, 5], 4: [5], 5: []}
    ```

1. Matrices de Adyacencia
    - Matrices de 2 dimensiones cuyas filas representan vertices de origen y columnas vertices de llegada.
    ```python
    grafo_no_dirigido = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [0, 1, 0, 1, 1], [0, 0, 1, 0, 1], [0, 0, 1, 1, 0]]
    grafo_dirigido    = [[0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
    ```

1. MAtrices de Incidencia
    - Matrices de 2 dimensiones cuyas filas representan vertices y columnas aristas (-1 es de llegada)
    ```python
    grafo_no_dirigido = [[1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]
    grafo_dirigido    = [[1, 0, 0, 0, 0], [-1, 1, 0, 0, 0], [0, -1, 1, 1, 0], [0, 0, -1, 0, 1], [0, 0, 0, -1, -1]]
    ```

#### Operaciones basicas:

- Las operaciones básicas que implementan estas estructuras de datos son:

    - **`adjacent(G, x, y)`** verifica que exista una arista entre `x` e `y`.

    - **`neighbors(G, x)`** entrega una lista con todos los vértices `y` tales que existe una arista entre `x` e `y`.

    - **`add_vertex(G, x)`** agrega el vértice `x`.

    - **`remove_vertex(G, x)`** remueve el vértice `x`.

    - **`add_edge(G, x, y)`** agrega una arista entre los vértices `x` e `y`.

    - **`remove_edge(G, x, y)`** remueve la arista entre `x` e `y`.

    - **`get_vertex_value(G, x)`** obtiene el valor asociado al vértice `x`.

    - **`set_vertex_value(G, x, v)`** asigna un valor al vértice `x`.

    - **`get_edge_value(G, x, y)`** retorna el valor asociado con la arista que existe entre `x` e `y`.

    - **`set_edge_value(G, x, y)`** asigna un valor a la arista que existe entre `x` e `y`.

#### DFS:

- Si un nodo no es visitado significa que  **no es alcanzable** desde el nodo de inicio
```python
def dfs(graph, start):
    # Vamos a mantener un set con los nodos visitados.
    visited = set()
    
    # El stack de siempre.
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        # Detalle clave: si ya visitamos el nodo, ¡no hacemos nada!
        if vertex not in visited:
            # Lo visitamos
            visited.add(vertex)
            # Agregamos los vecinos al stack si es que no han sido visitados.
            for v in graph[vertex]:
                if v not in visited:
                    stack.append(v)   
    return visited
```

#### BFS:

- Si un nodo no es visitado significa que  **no es alcanzable** desde el nodo de inicio
```python
from collections import deque

def bfs(graph, start):
    # Vamos a mantener un set con los nodos visitados.
    visited = set()
    # La cola de siempre.
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        # Detalle clave: si ya visitamos el nodo, no hacemos nada!
        if vertex not in visited:
            # Lo visitamos
            visited.add(vertex)
            # Agregamos los vecinos a la cola si es que no han sido visitados.
            for v in graph[vertex]:
                if v not in visited:
                    queue.append(v)
    return visited
```