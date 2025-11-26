# Tarea-Sockets

README – Chat Bidireccional en Python con Sockets

Este proyecto implementa un chat bidireccional entre un servidor y un cliente usando la librería estándar de Python: socket y threading.
La comunicación es en tiempo real, permitiendo que tanto el servidor como el cliente envíen y reciban mensajes simultáneamente.

El código está basado en el ejemplo visto en clase, manteniendo su estructura simple, pero agregando hilos para permitir el intercambio bidireccional.

¿Cómo funciona?

El sistema está compuesto por dos programas:

✔ server.py

Crea un socket servidor.

Acepta una conexión entrante.

Ejecuta un hilo encargado de recibir mensajes del cliente.

El hilo principal permite enviar mensajes al cliente.

✔ client.py

Se conecta al servidor.

Crea un hilo para recibir mensajes del servidor.

El usuario puede enviar mensajes desde la consola.

Gracias al uso de threading, ambos lados pueden leer y escribir al mismo tiempo, logrando un chat bidireccional real.

Requisitos

Solo necesitas:

Python 3.x

No se requieren librerías externas

🛠️ Instrucciones de uso
1️ Ejecuta el servidor

En una terminal:

python server.py


El servidor quedará escuchando conexiones.

2️ Ejecuta el cliente

En otra terminal:

python client.py


Una vez conectado:

El cliente puede escribir mensajes.

El servidor puede escribir mensajes.

Ambos verán los mensajes del otro en tiempo real.

 Flujo de comunicación

El servidor inicia y espera a un cliente.

El cliente se conecta.

Ambos crean un hilo secundario para recibir mensajes.

El hilo principal de cada lado permite escribir mensajes.

La conexión se mantiene abierta hasta que la aplicación se cierre.

 Estructura del proyecto
<img width="268" height="85" alt="image" src="https://github.com/user-attachments/assets/5d95d875-d5a3-4959-ae88-be3ed4acd412" />

Conceptos clave usados

Socket TCP

Se usa para crear la conexión entre cliente y servidor.

Hilos (threading)

Permiten que cada programa pueda:

Escuchar mensajes al mismo tiempo que escribe.

Evitar que la aplicación se bloquee esperando datos.

Comunicación bidireccional

Ambos lados pueden comunicarse simultáneamente sin esperar al otro.


Ejemlos de consola:
servidor:

<img width="483" height="273" alt="image" src="https://github.com/user-attachments/assets/f0b8758b-4e12-4a56-b1c8-80e7124090d2" />

cliente:

<img width="480" height="221" alt="image" src="https://github.com/user-attachments/assets/e89db3c1-7432-4288-9005-34afd51efc09" />

