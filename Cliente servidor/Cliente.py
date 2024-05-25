##############################################################################################################
# 
# 
#                                     Universidad Iberoamericana
# 
# 
#                                   Johan Sebastian Vega Rodriguez
# 
# 
#                                               Docente
#                                            Eduardo Solano
# 
# 
#                                       Arquitectura de software
#                                                 2024
#                                               
##############################################################################################################
 
##############################################################################################################
##                                                                                                          ##
##                                           Descripcion                                                    ##
##                                                                                                          ##
##############################################################################################################

"""
El presente proyecto se centra en el desarrollo de un sistema de chat cliente-servidor utilizando sockets 
TCP/IP en el lenguaje de programación Python. El objetivo principal de este proyecto es crear un entorno de 
chat simple pero funcional, donde múltiples usuarios puedan intercambiar mensajes en tiempo real a través 
de una conexión de red. El sistema consta de dos componentes principales: un servidor que gestiona las 
conexiones de los clientes y retransmite los mensajes entre ellos, y clientes individuales que se conectan 
al servidor para enviar y recibir mensajes
"""
"""
funciones:

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM): Establece la conexión del socket creado 
anteriormente con el servidor, utilizando la dirección IP y el puerto especificados.

thread_recv = threading.Thread(target=recibir_mensajes, args=(client_socket,)): Crea un hilo (thread_recv) 
que ejecutará la función recibir_mensajes, pasando como argumento el socket del cliente.

thread_recv.start(): Inicia la ejecución del hilo creado

client_socket.close(): Cierra el socket del cliente después de salir del bucle principal, liberando los 
recursos utilizados por la conexión con el servidor.
"""       
##############################################################################################################
##                                                                                                          ##
##                                           Librerias                                                      ##
##                                                                                                          ##
##############################################################################################################

import socket
import threading

##############################################################################################################
##                                                                                                          ##
##                                           Funciones                                                      ##
##                                                                                                          ##
##############################################################################################################

def recibir_mensajes(sock):
    while True:
        try:
            mensaje = sock.recv(1024).decode()
            print(mensaje)
        except ConnectionAbortedError:
            break

SERVER_ADDRESS = '192.168.140.51'
SERVER_PORT = 9090

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((SERVER_ADDRESS, SERVER_PORT))

thread_recv = threading.Thread(target=recibir_mensajes, args=(client_socket,))
thread_recv.start()

while True:
    mensaje = input("Yo: ")
    client_socket.sendall(mensaje.encode())
    if mensaje.lower() == "adios":
        break

client_socket.close()