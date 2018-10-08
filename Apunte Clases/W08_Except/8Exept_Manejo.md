15:30 02-10-2018

## Manejo de Excepciones
_By: Mahund_

#### Introduccion:

- Para **levantar** una excepcion se utiliza el comando **`raise`**

    ```python
    def dividir(num, den):
        if den == 0:
            # Aquí se genera la excepción y se incluye información 
            # con el significado de ella.
            raise ZeroDivisionError("El denominador es 0")
        return float(num) / float(den)
    ```
> Al ser anidables apenas se lanza excepción el resto del código no sigue ejecutándose y se termina el programa.

#### Manejo de Excepciones:

- Cada vez que se *lanza* una excepcion es posible **atraparla** utilizando `try`y `excecept`

- **try:** codigo perteneciente al *scope* de esta sentencia **no** se detiene independiende te si es lanzada alguna excepcion.

- **except:** codigo perteneciente al *scope* de esta sentencia es ejecutado dependiendo del tipo de *excepcion levantada*

- **else:** codigo perteneciente al *scope* de esta sentencia es ejecutado si no se ha levantado ningun *except* anterior (similar a if/elif/else, se ejecuta solo si try funciona correctamente)

- **finally:** codigo perteneciente al *scope* de esta sentencia siempre es ejecutado. Normalmente utilizado con funciones de *limpieza*: cerrar archivos, etc. 

##### Ejemplo:

```python
def dividir(num,den):
    if not (isinstance(num, int) and isinstance(den, int)):
        raise TypeError()

    if num < 0 or den < 0:
        raise ValueError("Valores negativos")

    return float(num)/float(den)


# Esta corresponde a la estructura completa de try and except
try:
    # Probamos si es posible realizar la operación
    resultado = dividir(10,0)
        
except (ZeroDivisionError, TypeError):
    # Este bloque opera para los tipos de excepciones definidos
    print("Revise los datos de entrada. ¡No son ints o bien el denominador es 0!")

except ValueError:
    # Este bloque sólo maneja excepciones del tipo ValueError
    print("Los valores ingresados son negativos")
        
else:
    # Como no hubo excepciones puede retornar normalmente el resultado
    # En este caso, si se coloca un return después de la operación y
    # esta es correcta, entonces nunca llegará a este punto.
    print("¡Todo OK!, no hay errores con los datos")
        
finally:
    print("Recuerde SIEMPRE usar excepciones para manejar los errores de su programa\n")
```

#### Crear Excepciones:

- Todas las excepiones son *objetos* que heredan de la clase **Exception**, la cual en conjunto con *KeyboardInterrupt* y *SystemExit* heredan de *BaseException*.

- Se puede *generalizar* el error utilizando Exception:
    
    ```python
    try:
        print(dividir(4,0))
    
    except Exception as err:
        # Este bloque opera para todos los tipos de excepciones que hereden de Exception
        print(f"Error: {err}")
        print("Revise los datos de entrada"
    ```

##### Excepcion personalizada:

1. Redefiniendo metodos:

    ```python
    class Excepcion1(Exception):
        # Al no sobreescribir nada, hereda todo sin modificaciones
        pass


    class Excepcion2(Exception):
        def __init__(self, a, b):
            # Sobreescribimos el __init__ para cambiar el ingreso de los parámetros
            super().__init__(f"Alguno de los valores {a} o {b} no es entero\n")


    def dividir(num,den):
        # Por ejemplo, redefiniremos las excepciones que
        # utilizamos en los ejemplos anteriores.
        if not (isinstance(num, int) and isinstance(den, int)):
            raise Excepcion2(num, den)

        if num < 0 or den < 0:
            raise Excepcion1("Los valores son negativos\n")

        return float(num) / float(den)
    ```

1. Creando nuevos metodos:

    ```python
    class ErrorTransaccion(Exception):
        
        def __init__(self, fondos, gasto):
            super().__init__(f"El dinero en la billetera no alcanza para pagar ${gasto}")
            self.fondos = fondos
            self.gasto = gasto
        
        def exceso(self):
            return self.gasto - self.fondos

        
    class Billetera:
        
        def __init__(self, dinero):
            self.fondos = dinero
        
        def pagar(self, gasto):
            if self.fondos - gasto < 0:
                raise ErrorTransaccion(self.fondos, gasto)
            self.fondos -= gasto

            
    b = Billetera(1000)

    try:
        b.pagar(1500)

    except ErrorTransaccion as err:
        print(f"Error: {err}. Hay un exceso de gastos de ${err.exceso()}.")
    ```

#### Conclusion:

En general, las principales ventajas de usar excepciones por sobre if-else son:

1. El programador está obligado a darles algún tratamiento, es decir, manejarlas o levantarlas. Mientras que los códigos de error pueden ser erróneamente ignorados por el programador.

1. El código queda más limpio.

1. Todas las situaciones del programa son manejadas genéricamente, mientras que usando códigos de error tenemos la obligación de crear estructuras de control para cada función que implementemos.

1. El manejo de excepciones permite "notificar" a otras aplicaciones sobre este tipo de situaciones, lo que no sería tan simple de lograr usando códigos de error inventados por el programador.

1. ¿Porqué importa que el programa no falle inesperadamente?: Muchas veces exponer errores que no se han manejado a usuarios finales puede ser peligroso, ya que se podrían visualizar trozos de código en los outputs de estos.