19:43 13-11-2018

## Serializacion
_By: Mahund_

#### Introduccion:

- Hostname: Direccion del edificio (puede ser `"www.gogle.com"` o `"10.00.00.21"`).

- Puerto: Numero del departamento (son ints)

- Protocolos: TCP vs UCP

    - TCP: Necesita estar conectado al servidor, es lento pero confiable. (Utilizado en aplicaciones que no pueden perder informacion: WSP, Mails, etc).

    - UDP: No necesita conexiones (servidor envia informacion haya o no cliente). Es rápido pero no es confiable. (Utilizado en juegos online, streamings, etc).

- Sockets: objeto en python que encapsula comunicacion y conexion.

    - Recibe tipo de ip (v4 o v6) y protocolo (TCP o UDP)

- TCP Socket (Foto): 
    - listen recibe numero maximo de conexiones simultaneas
    - accept detiene el programa hasta que un cliente intenta conectarse
    - send envia bytes al cliente
    - recv detiene el programa hasta que servidor reciba algo del cliente

- UDP Socket (Foto)
    - No es importante