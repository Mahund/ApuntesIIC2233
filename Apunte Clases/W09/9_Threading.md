19:43 08-10-2018

## Threading
_By: Mahund_

#### Introduccion:

- Los sistemas operativos (*so*) modernos tienen una variedad de *procesos* corriendo simultaneamente.

- Tal paralelismo es una **ilusion**, en realidad el so **comparte la cpu**: avanza un poco en un proceso, lo pausa, avanza en otro, la pausa, vuelve al primero, etc.

- Mientras más *nucleos* mas tareas **realmente** en paralelo se pueden realizar.

#### Threads:

- Cada *thread* es un **hilo**: unidad más pequeña que puede ser programadas para ser ejecutadas en un so.

- Los threads dentro de un mismo proceso **comparten memoria**, lo que les permite ejecutarse más rapido que corres varias instancias del mismo programa.

- Un proceso puede tener 1 o varioas threads, que seran ejecutados **como tareas en paralelo** (simulado).

- Se utiliza **time slicing**:
    
    1. Se toma un thread de aquellos en espera
    1. Se ejecuta cierto numero de instrucciones de tal thread
    1. Se deja thread en espera
    1. Se repite proceso con nuevo thread

> En os con procesador de un solo nucleo: no se logra aumento de velocidad pero si de la manera en que programa responde.

- Buenos ejemplos para utilizar threads:

    - Interfaces de respuesta rapida: se necesita interactuar con usuario mientras se ejecuta codigo
    - Delegacion de trabajos: aquellos con patron de productor/consumidor
    - Aplicaciones multiuso: cada hilo atiende peticiones de un usuario diferente (servidor paginas web)

#### Threads en Python:

- Se utiliza libreria `threading`:
    
    - `Thread`: representa un hilo
    - `target`: parametro que representa funcion que ejecutara el hilo
    - `name`: parametro que representa nombre del hilo
    - `args` o `kwargs`: permiten entregar parametros a los hilos
    - `start()`: metodo para ejecutar el hilo

- Ej:

```python
import threading
import time


def worker(tiempo):
    current_thread = threading.current_thread()
    print(f"{current_thread.name} partiendo...")
    # Pondremos a dormir el thread por 2 segundos simulando 
    # que ocurre algun proceso dentro de la función
    time.sleep(tiempo) 
    print(f"{current_thread.name} terminando...")

def service(tiempo):
    current_thread = threading.current_thread()
    print(f"{current_thread.name} partiendo...")
    # Ponemos a dormir el thread por 4 segundos simulando
    # un proceso dentro de la función
    time.sleep(tiempo) 
    print(f"{current_thread.name} terminando...")


# Creamos los threads usando la clase Thread
t1 = threading.Thread(name="Thread 1", target=service, args= 3)
w1 = threading.Thread(name="Thread 2", target=worker, kwargs={"tiempo": 3})
w2 = threading.Thread(target=worker)  # En este caso usa el nombre asignado por defecto

# Se inicializan los threads creados
w1.start()
w2.start()
t1.start()

# Todas estas líneas serán ejecutadas mientras los threads se ejecutan independientemente 
# del programa principal
print("Fueron creados 3 threads")
for i in range(10):
    print(i)
```

- Podemos heredar y hacer override sobre metodo `run()`, quien se ejecuta luego de `start()`

```python
import threading
import time


class Worker(threading.Thread):
    """Este será nuestro nuevo Worker basado en Thread"""
    def __init__(self, tiempo):
        # En el caso de los threads, lo primero es invocar al init original.
        super().__init__()
        self.tiempo = tiempo
    
    def run(self):
        # Este metodo ejecuta el proceso de este thread
        # cuando lo iniciamos mediante el metodo start()
        print(f"{self.name} partiendo...")
        tiempo_partida = time.time()
        time.sleep(self.tiempo) 
        print(f"{self.name} terminando después de {time.time() - tiempo_partida} seg.")

        
class Service(threading.Thread):
    """Este sera el nuevo Service basado en Thread"""
    def __init__(self, tiempo):
        super().__init__()
        self.tiempo = tiempo
    
    def run(self):
        print(f"{self.name} partiendo...")
        tiempo_partida = time.time()
        time.sleep(self.tiempo) 
        print(f"{self.name} terminando después de {time.time() - tiempo_partida} seg.")
        

# Se crean los threads, name podria ser un parametro como tiempo
t1 = Service(3)
t1.name = "Servicio 3"
w1 = Worker(4)
w1.name = "Trabajador 4"
w2 = Worker(5)
w2.name = "Trabajador 5"

# Se inicializan los threads creados
w1.start()
w2.start()
t1.start()

# Todas estas líneas serán ejecutadas mientras los threads se ejecutan independientemente
# del programa principal.
print("Fueron creados 3 threads")
for i in range(10):
    print(i)
```

- Si se necesita que programa principal espere termino de algun thread se ocupa metodo `join(timeout=None)`, si no se define timeout el programa principal esperara hasta que thread haya terminado, sino esperar timeout segundos desde que inicia espera (al terminar join anterior).

- Si ademas queremos ver si thread sigue ejecutandose (sigue vivo) utilizamos `is_alive()`

```python
import threading
import time

# Usamos la definicion de los Thread declarados en el ejemplo anterior
# Se crean los threads usando la clase Thread.
t1 = Service(1)
w1 = Worker(6)
w2 = Worker(10)

# Se inicializan los threads creados
t1.start()
w1.start()
w2.start()

# Aquí incorporamos el método join() para bloquear el programa principal
t1.join()     # No especificamos timeout, esperará lo que sea necesario
w1.join()     # Esperaremos lo que sea necesario.
w2.join(3)  # Esperaremos máximo 8.8 segundos.

# En este punto, el programa ha esperado por los tres threads que creamos
# Estas líneas serán ejecutadas después de que los threads hayan terminado

print("Fueron creados 3 threads")
for i in [t1,w1,w2]:
    print(i.is_alive())
```

- Parametro `daemon` al ser True permite que programa termine aunque thread no haya terminado su ejecucion.
> Puede utilizarse `join()` para obligar a programa a esperar un *daemon thread*.  
> Una vez iniciado el thread mediante `start()` no se puede editar parametro `daemon`.

- Clase `Timer`es subclase de `Thread` y permite ejecutar thread despues de ciertos segundos.

```python
def mi_timer(archivo):
    with open(archivo) as fid:
        for linea in fid:
            print(linea)

t1 = threading.Timer(10.0, mi_timer, args=("files/mensaje_01.txt",))
t2 = threading.Timer(5.0, mi_timer, kwargs={"archivo": "files/mensaje_02.txt"})

t1.start() # el thread t comenzará después de 10 seconds
t2.start() # el thread t comenzará después de 5 seconds
```