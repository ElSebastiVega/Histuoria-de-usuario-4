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

c.sendall(f"Cliente {cliente_address}: {mensaje}".encode()): Envía el mensaje a todos los otros clientes 
conectados.

cliente_socket.close(): Cierra la conexión con el cliente.

clientes.remove(cliente_socket): Elimina el socket del cliente de la lista de clientes conectados.

SERVER_ADDRESS: Define la dirección IP del servidor.

SERVER_PORT = Define el puerto del servidor.

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM): Crea un socket TCP/IP.

server_socket.bind((SERVER_ADDRESS, SERVER_PORT)): Vincula el socket a la dirección y puerto del servidor.

server_socket.listen(5): Empieza a escuchar por conexiones entrantes, con un máximo de 5 conexiones en cola.

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

clientes = []

def manejar_cliente(cliente_socket, cliente_address):
    while True:
        try:
            mensaje = cliente_socket.recv(1024).decode()
            if not mensaje:
                break
            print(f"Cliente {cliente_address}: {mensaje}")
            for c in clientes:
                if c != cliente_socket:
                    c.sendall(f"Cliente {cliente_address}: {mensaje}".encode())
        except ConnectionResetError:
            break
    cliente_socket.close()
    clientes.remove(cliente_socket)

# Configuración del servidor

SERVER_ADDRESS = '192.168.140.51'
SERVER_PORT = 9090

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((SERVER_ADDRESS, SERVER_PORT))

server_socket.listen(5)
print("Servidor listo para recibir conexiones...")

# Ciclo principal para manejar las conexiones de los clientes

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Cliente conectado desde {client_address}")
    clientes.append(client_socket)
    thread_cliente = threading.Thread(target=manejar_cliente, args=(client_socket, client_address))
    thread_cliente.start()
