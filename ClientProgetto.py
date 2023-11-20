import socket

HOST = 'localhost'  
PORT = 50000             
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    data = s.recv(1024)

    if(data.decode()=="STOP"):
        print("Tentativi esauriti. Disconnessione.")
        break
    subs=":"
    if(data.decode()=="5"):
        break
    print(data.decode())
    if  data.decode().find(':') or data.decode().find('.'):
        testo = input("").encode()
        s.send(testo)


s.close()