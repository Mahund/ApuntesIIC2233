19:43 08-10-2018

## Concurrencia
_By: Mahund_

#### Introduccion:

- Polling: revisar activamente cada elemento de la interfaz, es muy costoso ya que muchas veces no habra accion a realizar.

- Arquitectura basada en eventos: un evento es una accion que ocurre en el programa, ya sea por el usuario o por otra parte del programa. Se puede definir comportamiento del programa mediante funciones que se hacen cargo de un evento de forma **asincrona**.
    1. Para cada evento **e** definimos una funcion **e_handler** que se ejecuta al ocurrir evento **e**.
    1. Programa debe detectar ocurrencia de **e** y asi ejecutar **e_handler**

#### PyQt:

- Modulos basicos:

    - **QtWidget**: contiene las clases que brindan los elementos clásicos de interfaces gráficas para aplicaciones en desktop PCs.
    - **QtCore**: incluye las clases para funcionalidades no-GUI, como: ciclo de eventos, manejo de archivos, tiempo, threads, etc.
    - **QtGui**: contiene las classes con componentes para integración de ventanas, manejo de eventos, etc.
    - **QtNetwork**: provee las clases para crear aplicaciones gráficas en entornos de red basadas en TCP/IP, UDP.
    - **QtOpenGL**: incluye las clases para el uso de OpenGL durante renderizado 3D.
    - **QtSvg**: provee de clases para mostrar archivos de gráficos vectoriales (SVG).
    - **QtSql**: incluye funcionalidades para el trabajo con bases de datos SQL.
    - **QtBluetooth**: contiene clases que permiten la búsqueda e interacción con dispositivos a través de bluetooth.

- Creacion de una ventana: clase `QWidget` desde el módulo `QtWidgets`. 
