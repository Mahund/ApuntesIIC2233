19:43 15-11-2018

## Networking
_By: Mahund_

#### Tips:

- Entornos virtuales: permiten tener la misma libreria (por ejemplo) con distintas versiones para cada proyecto.

- Crear entorno: `py -m venv folder_name`, `source venv/bin/activate`

#### Introduccion:

- Se utiliza para comunicarse con alguien más (redes).

- Encapsulamiento: OSI o TCP/IP

    - OSI: utiliza 7 capas (Application, Presentation, Session, Transport, Network, Data link, Physical)
    - TCP: utiliza 4 capas (Application, Transpot, IP, Link)

- IP: direccion que identifica al computador, existe version 4 y 6.

- Puerto: identifica a la aplicacion

- Protocolos de transporte: TCP p UDP

    - TCP: orientado a conexion, verifica que todos los paquetes sean recibidos, lento por overhead.
    - UDP: no orientado a conexion, no verifica recepcion, rápido.

- Arquitecturas: Cliente-Servidor

- Protocolos de aplicacion:

    - Como se envian los mensajes
    - Que debe tener el mensaje
    - Como identificar mensaje