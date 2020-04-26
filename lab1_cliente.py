import socket

enchufe=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
enchufe.connect((socket.gethostname(),1234))

mensaje=enchufe.recv(1024)
print(mensaje.decode("utf-8"))
print("Ingrese la URL de la cual desea obtener el header: ")
URL=input()
enchufe.send(bytes(URL,"utf-8")) #le mandamos la URL al servidor
