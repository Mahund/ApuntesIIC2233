14:30 19-09-2018

## Arboles
_By: Mahund_

#### Definiciones:

- **Arbol:** estructura de datos *no lineal* guiada por una estructura **jerarquica** (*padre-hijo*)

- **Nodo raiz:** primer nodo del arbol (padre de todos)

- **Nodo hoja:** nodo que no posee hijos

- **Arista:** conexion directa entre un par de nodos

- **Camino:** secuencia ordenada de nodos consecutivos unidos por aristas

- **Profundidad:** numero de aristas que deben recorrerse desde un nodo para llegar al nodo raiz

- **Altura:** profundidad maxima entre las hojas de un arbol

#### Propiedades:

1. Si el arbol no esta vacio, entonces tiene un *unico nodo raiz* que no posee padre

1. Cada nodo en el arbol distinto de la raiz tiene un unico padre, y todos los nodos que compartan un padre son hijos de el.

##### Ejemplo de Arbol:

```python
# textwrap tiene varias funciones convenientes para el manejo de strings
from textwrap import indent

class Arbol:
    """
    Esta clase representa un árbol
    
    La estructura es recursiva, de manera que cada nodo es la raíz de un sub-árbol.
    Los nodos hijos pueden ser guardados en una estructura, como lista o diccionario.
    En este ejemplo, los nodos hijos serán guardados en un diccionario.
    """

    def __init__(self, id_nodo, valor=None, padre=None):
        """
        Inicializa la estructura básica del árbol.
        
        Tiene un identificador propio, la referencia a su padre, el valor almacenado
        y una estructura con sus hijos.
        """
        self.id_nodo = id_nodo
        self.padre = padre
        self.valor = valor
        self.hijos = {}
        

    def obtener_nodo(self, id_nodo):
        """
        Obtiene el nodo con el id dado, en forma recursiva
        
        A partir del nodo actual, buscamos el nodo 'id_nodo' entre sus hijos
        y lo retornamos si existe.
        """
        # Caso base: ¡Lo encontramos!
        if self.id_nodo == id_nodo:
            return self

        # Buscamos recursivamente entre los hijos
        for hijo in self.hijos.values():
            nodo = hijo.obtener_nodo(id_nodo)
            # Si lo encontró, lo retornamos
            if nodo:
                return nodo
        
        # Si no lo encuentra, retorna None
        return None


    def agregar_nodo(self, id_nodo, valor, id_padre):
        """Agrega un nodo con el id y valor dado, como hijo del nodo con el id 'id_padre'"""
        # Primero, tenemos que encontrar al padre
        padre = self.obtener_nodo(id_padre)
        # En caso de que el padre no exista no hacemos nada
        if padre is None:
            return
        
        # Creamos el nodo
        # Nos aseguramos de que el nodo nuevo sea del mismo tipo que la raíz
        # Esto lo ocuparemos cuando heredemos de este árbol
        nodo = type(self)(id_nodo, valor, padre)
        # Agregamos el nodo como hijo de su padre
        padre.hijos[id_nodo] = nodo
        
        
    def __repr__(self):
        """
        Entrega una representación del árbol, en forma recursiva.
        
        Para ello, tenemos que pedir la representación de cada hijo recursivamente. 
        Esto nos lleva a recorrer todos los nodos del árbol.
        """
        # Texto de este nodo.
        # Si el nodo es hoja, se avisa de ello.
        # Si el nodo no es hoja, se deja un salto de línea para poder nombrar a los hijos.
        if self.hijos:
            texto = f"id: {self.id_nodo}, valor: {self.valor}\n"
        else:
            texto = f"id: {self.id_nodo}, valor: {self.valor}, nodo hoja"

        # Extrae el repr a cada hijo, en forma recursiva.
        texto_hijos = [repr(hijo) for hijo in self.hijos.values()]
        
        # Indentamos cada línea del texto de los hijos con dos espacios.
        # Esto es para que se note el nivel del nodo.
        texto_hijos = [indent(x, "  ")  for x in texto_hijos]
        
        return texto + "\n".join(texto_hijos)
```

#### Recorridos Arbol:

1. Breadth First Search (BFS)

1. Depth First Search (DFS)

##### BFS Recorrido por Amplitud:

- Recorre el arbol por niveles: padres, hijos, hijos de hijos, etc
> Utiliza estructura de **Cola/Queue** para almacenar nodos sin visitar, implementa `__iter__`

```python
from collections import deque

class ArbolBFS(Arbol):
    """Heredamos de la clase Arbol para hacerla iterable según el orden con BFS"""
    
    def __iter__(self):
        """Itera el árbol según BFS"""
        # Utilizamos una cola para almacenar los nodos por visitar
        cola = deque()
        # El primer nodo a visitar será la raíz
        cola.append(self)
        
        # Mientras queden nodos por visitar en la cola
        while cola:
            # Extraemos el primero de la cola
            nodo = cola.popleft()
            
            # Lo visitamos
            yield nodo
            
            # Agregamos todos los nodos hijos a la cola
            for hijo in nodo.hijos.values():
                cola.append(hijo)
```
> Este tipo de arbol no posee ciclos, por esto no se revisa si un nodo fue visitado 2 veces

##### DFS Recorrido por Profundidad:

- Recorre el arbol por ramas: Padre, primer hijo, primer hijo del primer hijo, etc
> Utiliza estructura de **Pila/Stack** para almacenar nodos sin visitar, implementa `__iter__`

```python
from collections import deque

class ArbolDFS(Arbol):
    """Heredamos de la clase Arbol para hacerla iterable según el orden con DFS"""
    
    def __iter__(self):
        """Itera el árbol según DFS"""
        # Utilizamos un stack para almacenar los nodos por visitar
        stack = deque()
        # El primer nodo a visitar será la raíz
        stack.append(self)
        
        # Mientras queden nodos por visitar en el stack
        while stack:
            # Extraemos el que está en el tope del stack
            nodo = stack.pop()
            
            # Lo visitamos
            yield nodo
            
            # Agregamos todos los nodos hijos al stack
            for hijo in nodo.hijos.values():
                stack.append(hijo)
```

- **DFS Recursivo:** se puede utilizar recursivamente

```python
from collections import deque

class ArbolDFSRecursivo(Arbol):
    """Heredamos de la clase Arbol para hacerla iterable según el orden con DFS recursivo"""
    
    def __iter__(self):
        """Itera el árbol según DFS recursivo"""
        # Visitamos el nodo actual
        yield self
        # Aplicamos esto recursivamente a cada hijo
        for hijo in self.hijos.values():
            yield from hijo
```

#### Arbol binario:

- Caso particular de arbol donde:
    1. Cada nodo tiene **2 hijos maximo**
    1. Cada hijo esta etiquetado como *hijo izquierdo o hijo derecho*
    1. El hijo **izquierdo** precede al *derecho*
> El nivel `d` posee `2**d hijos`

- Arbol binario **completo:** cuando todos los nodos poseen exactamente **2** hijos, y todos los *nodos hojas* estan en el **mismo nivel**
> Nodos totales: `2**(d+1) - 1` con d profundidad maxima

##### Arbol Binario en nodos enlazados

- Se agrega la regla que hijo izquierdo es para valores **menores o igual** al valor del padre, y hijo derecho es para valores **mayores**

```python
class ArbolBinario:
    """Modela un árbol binario"""

    def __init__(self, valor=None, padre=None):
        """
        Inicializa un árbol binario
        
        El valor es opcional y se puede llenar con el primer nodo que se intente agregar.
        """
        self.valor = valor
        self.padre = padre
        self.hijo_izquierdo = None
        self.hijo_derecho = None
    
    def agregar_nodo(self, valor):
        """
        Agrega un nodo nuevo con el valor dado siguiendo ciertas reglas, recursivamente
        
        Vamos a implementar la regla de que el 'hijo_izquierdo' debe ser menor o igual
        que el valor del nodo, y que el 'hijo_derecho' debe ser mayor.
        
        Como la regla se implementa recursivamente, el árbol que estamos armando tiene
        la siguiente propiedad: todo nodo en el subárbol izquierdo tiene un valor menor
        o igual al actual, y todo nodo en el subárbol derecho tiene un valor mayor al actual.
        """
        # Si no teníamos valor en el nodo (al crear el árbol), lo ponemos acá
        if self.valor is None:
            self.valor = valor
            return
        
        # Si el valor es menor o igual, revisamos el hijo izquierdo
        if valor <= self.valor:
            # Si no existe el hijo izquierdo, lo creamos con ese valor y terminamos
            if not self.hijo_izquierdo:
                self.hijo_izquierdo = ArbolBinario(valor, self)
            # Si existe, le delegamos la labor de agregar el nodo
            else:
                self.hijo_izquierdo.agregar_nodo(valor)
        # Este es el caso en que el valor es mayor al actual
        else:
             # Si no existe el hijo derecho, lo creamos con ese valor y terminamos
            if not self.hijo_derecho:
                self.hijo_derecho = ArbolBinario(valor, self)
            # Si existe, le delegamos la labor de agregar el nodo
            else:
                self.hijo_derecho.agregar_nodo(valor)
                
    def __repr__(self):
        """Entrega una representación del árbol, en forma recursiva"""
        texto = f"Valor: {self.valor}"
        texto_izquierdo = indent(repr(self.hijo_izquierdo), "  ")
        texto_derecho = indent(repr(self.hijo_derecho), "  ")
        
        return "\n".join([texto, texto_izquierdo, texto_derecho])
```