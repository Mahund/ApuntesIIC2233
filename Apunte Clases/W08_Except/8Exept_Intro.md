19:30 01-10-2018

## Excepciones
_By: Mahund_

#### Introduccion:

- Excepciones son *lanzadas* cuando ocurren *errores* que interrumpen el flujo normal del programa durante su *tiempo de ejecucion*.

- Al *atrapar* una excepcion es posible *controlar errores* y prevenir que se **caiga** el programa.

- Durante el *tiempo de interpretacion* se revisa validez de una linea
> Lenguajes *compilados* a diferencia permiten lanzar excepciones prematuras

- Los errores son objetos

#### Tipos de Excepciones:

1. **SyntaxError:** lanzada cuando sentencia esta **mal escrita**
    ```python
    print "hola"
    ```

1. **NameError:** lanzada cuando se intenta utilizar nombre no definido
    ```python
    a = variable_sin_definir
    ```

1. **ZeroDivisionError:** lanzada cuando se intenta divir por 0
    ```python
    print(2/0)
    ```

1. **IndexError:** lanzada cuando se intenta ingresar a index inexistente
    ```python
    a = [1,2,3]
    print(a[3])
    ```

1. **TypeError:** lanzada cuando se intenta utilizar funcion con parametros erroneos
    ```python
    print(1 + [2,3]) 
    ```

1. **AtributeError:** lanzada cuando se intenta utilizar metodo o atributo inexistente de una clase
    ```python
    a = Humano()
    print(a.volar())
    ```

1. **KeyError:** lanzada cuando se intenta ingresar a key invalida de diccionario
    ```python
    dicc = {1: 1, 2: 2}
    print(dicc[3])
    ```
