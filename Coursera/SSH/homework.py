#ssh pi@192.168.0.15

import socket
ms = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ainfo = socket.getaddrinfo(None , 5555)
#si error cambiar el puerto
print (ainfo)
#aqui tengo que buscar la direccion ip y el puerto, algo como ('127.0.0.1', 1234)
print (ainfo[5][4])
ms.bind (ainfo[5][4])
ms.listen(5)
conn, addr = ms.accept()

#here I need to write in a new terminal : nc 127.0.0.1 5555 

while(True):
        data = conn.recv(1000)
        if data:
           print ("Got a request!")






