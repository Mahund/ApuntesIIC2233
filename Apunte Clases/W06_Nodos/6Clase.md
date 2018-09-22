20-09-2018

## Nodos y Arboles
_By: Mahund_

#### Introduccion:

- Usos de terminal:
    1. Alias: permite definir *atajos* (Ocupar zsh)
    1. Comandos: `ls, mkdir, cd, git init, ls -a, touch, status, atom`
    1. Ejecutar Py y permitir escribir sobre el: `py -i file.py`

#### Estructura de Datos:

- **Nodo:** unidad basica de los datos

- **Lista ligada:** nodos conectados de forma secuencial, cada nodo posee name y siguiente.
    - Ventajas:
        1. No necesita conocer *a priori* cantidad de elementos
        1. Inserciones rápidas
    - Desventajas:
        1. Acceso secuencial
        1. No se puede retroceder al recorrerla

- **Lista doblemente ligada:** nodos que poseen name, siguiente y anterior.
    - Permiten retroceder
> Un ejemplo serian los deques

- **Arboles:** nodos con diferentes *jerarquias*, de orden padre-hijo
    - **BFS** vs **DFS**:
        1. BFS: recorre por nivel utilizando colas
        1. DFS: recorre por profundidad utilizando stacks
    - Arbol Binario:
        1. 2 hijos maximo

- **Recursion vs Iteracion:** recursion es no optimizada, pero es mas elegante