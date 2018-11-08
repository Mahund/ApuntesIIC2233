19:43 08-10-2018

## Concurrencia
_By: Mahund_

#### Introduccion:

- Intentar modificar **concurrentemente** un mismo valor con 2 o más threads sin precauciones generará un error.

- Hay que asegurarse que las operaciones a realizar sean **atomicas** (que un thread no la realice a menos que ningún otro la esté haciendo).

- Un conjunto de instrucciones que debe ser atomico se denomina **seccion critica**.

#### Sincronizacion:

- Existen 2 metodos para sincronizar 2 o más threads:

##### Locks:

- Se utiliza para que un solo thread este en una seccion critica a la vez.

- Puede estar *bloqueado o desbloqueado*:
    - Se bloquea mediante `acquire()`
    - Se desbloquea mediante `release()`

- El metodo `with` permite realizar el bloqueo y desbloque de forma automática.

```python
global_lock = threading.Lock()

def worker_con_seccion_critica(counter):
    for _ in range(10 ** 6):
        with global_lock:
            # --- Sección crítica ---. 
            # Está garantizado que en estas líneas sólo habrá un thread a la vez.
            counter.value += 1
            # --- Fin de la sección crítica ---.
```
> threds deben compartir el recurso lock

##### Events:

- Se utiliza para el *envio de señales* entre diferentes threds

- Su `flag` es un booleano y se accede mediante:
    - Se envia con `set()`
    - Se recibe en `wait()`
    - Se resetea con `clear()`

```python
# Ejemplo sacado de http://zulko.github.io/blog/2013/09/19/a-basic-example-of-threads-synchronization-in-python/

import threading
import time

# Tenemos dos eventos o señales.
# Esta es para avisar que el video ya está listo para ser reproducido.
video_cargado = threading.Event()
# Esta es para avisar que el audio ya está listo para ser reproducido.
audio_cargado = threading.Event()

def reproducir_video(nombre):
    print(f"Cargando video {nombre} en t={time.time():.6f}")
    # Supongamos que se demora 3 segundos
    time.sleep(3)
    print(f"Video cargado! en t={time.time():.6f}")
    # Avisamos que el video ya está cargado
    video_cargado.set()
    # Esperamos a que el audio ya se haya cargado
    audio_cargado.wait()
    # Listo!
    print(f"Reproduciendo video en t={time.time():.6f}")
    
    
def reproducir_audio(nombre):
    print(f"Cargando audio {nombre} en t={time.time():.6f}")
    # Supongamos que se demora 5 segundos
    time.sleep(10)
    print(f"Audio cargado! en t={time.time():.6f}")
    # Avisamos que el audio ya está cargado
    audio_cargado.set()
    # Esperamos a que el video ya se haya cargado
    video_cargado.wait()
    # Listo!
    print(f"Reproduciendo audio en t={time.time():.6f}")
    
    
t1 = threading.Thread(target=reproducir_audio, args=("dummy",))
t2 = threading.Thread(target=reproducir_video, args=("dummy",))

t1.start()
t2.start()

t1.join()
t2.join()
```
> Tener mucho ojo para evitar **deadlocks**, donde se genera un loop imposible de salir (por ejemplo se espera un señal antes de enviar la propia).

#### Ejemplos y aplicaciones

1. Lock como subclase de Thread

```python
import threading
import time
from random import random


class EscritorArchivo(threading.Thread):
    """
    Esta clase modela un thread. Dentro creamos un objeto para bloqueo dentro de la clase. 
    El Lock es una variable independiente de cada thread
    """
    
    lock = threading.Lock()
    
    def __init__(self, numero, archivo):
        super().__init__()
        self.name = f"EscritorArchivo número {numero}"
        self.numero = numero
        self.archivo = archivo
    
    def run(self):
        # Recordemos que la forma de buscar atributos es:
        # 1. Buscar en la instancia (en este caso, no existe).
        # 2. Si no existe, buscar en la clase (en este caso, lo encuentra).
        # 3. Si no existe, error.
        with self.lock:
            try:
                self.archivo.write(f"Línea escrita por thread # {self.numero}\n")
            finally:
                # Hacemos que se demore una cantidad random uniforme [0, 1)
                time.sleep(8*random())
                

# Creamos un archivo para escribir una salida. 
# Luego creamos los threads que escribirán dentro del archivo
with open("files/salida.txt", "w", encoding="UTF-8") as archivo:
    # Creamos los threads
    cantidad_threads = 7
    threads = [EscritorArchivo(i, archivo) for i in range(cantidad_threads)]
    
    # Hacemos partir los threads
    for thread in threads:
        thread.start()

    # Esperamos a todos los threads antes de cerrar el archivo
    for thread in threads:
        thread.join()
```

1. Productor/Consumidor con Queues

    - `put()`: Agrega un ítem al final de la cola (_push_)
    - `get()`: Remueve y retorna un ítem de la cola (_pop_). Lo interesante es que este método **espera** hasta que exista algo para sacar de la cola.
    - `task_done()`: Requiere ser llamado cada vez que un ítem extraído de la cola ha sido procesado.
    - `join()`: El _thread_ que llame a este método queda en pausa hasta que todos los ítems de la cola hayan sido procesados.

```python
from queue import Queue
from random import choice
import threading
import time

piezas_de_pan = Queue()

def panadero():
    # El panadero hará 2 veces pan
    for partida in range(2):
        # En cada vez, producirá 5 piezas de pan.
        # Se demorará 5 segundos por vez (que rápido :D)
        time.sleep(5)
        print("Produje 5 piezas de pan en la partida", partida)
        for _ in range(5):
            piezas_de_pan.put(choice(["Marraqueta", "Baguette", "Hallulla"]))


def cliente():
    mi_pan = piezas_de_pan.get()
    print(f"Saqué mi {mi_pan}!")
    piezas_de_pan.task_done()


thread_panadero = threading.Thread(target=panadero)
threads_clientes = [threading.Thread(target=cliente) for _ in range(10)]

thread_panadero.start()
for thread_cliente in threads_clientes:
    thread_cliente.start()
```