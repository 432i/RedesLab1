import socket
import time

enchufe=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
enchufe.bind((socket.gethostname(),1234))
enchufe.listen(5)
while True:
    enchufeDelCliente, direccion = enchufe.accept() #objeto que represeta el cliente
    print(f"Se ha establecido una conexión desde la dirección {direccion} de manera correcta.")
    enchufeDelCliente.send(bytes("Bienvenido al servidor XD!!","utf-8"))
    URL=enchufeDelCliente.recv(1024) #URL que manda el cliente
    URL=URL.decode("utf-8")          #ojo aki
    print("URL recibida de forma exitosa.")
    print("Buscando header de la URL...")
    #aqui realizamos una conexion con la página que pide el cliente
    enchufeURL=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    enchufeURL.connect((str(URL),80))
    enchufeURL.send(b"GET / HTTP/1.1\r\nHost: {URL}\r\n\r\n")
    HEADER=enchufeURL.recv(10000)
    HEADER=HEADER.decode("utf-8")
    print("El header de la URL solicitada es:\n",HEADER)



    '''while True:
        time.sleep(2)
        enchufeDelCliente.send(bytes("hola!","utf-8"))
        time.sleep(2)
        enchufeDelCliente.send(bytes("hola??","utf-8"))
    '''