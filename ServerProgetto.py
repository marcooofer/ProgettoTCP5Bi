import socket
import mysql.connector
import sys

pw = "Facile"

cono = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Progetto_Marco_Ferrari",
    port=3306,
    )

cur = cono.cursor()

def Lettura(a):
    if a=="1":
        query = "SELECT * FROM dipendenti"
        cur.execute(query)
        dato = cur.fetchall()
    if a=="2":
        query = "SELECT * FROM zone_di_lavoro"
        cur.execute(query)
        dato = cur.fetchall()
    return dato

def Elimina(a):
    if a=="1":
        conn.send("Inserisci l'id da rimuovere: ".encode())
        nome=(conn.recv(1024)).decode()

        query = (f"DELETE FROM dipendenti where IDdip = '{nome}'")
        print(nome)
        print(query)
        cur.execute(query)
        cono.commit()
        dato = "Rimozione andata a buon fine."
    if a=="2":
        conn.send("Inserisci l'id della zona da rimuovere: ".encode())
        nome=(conn.recv(1024)).decode()
        print(nome)
        query = (f"DELETE FROM zone_di_lavoro where IDzona = '{nome}'")
        print(query)
        cur.execute(query)
        cono.commit()
        dato = "Rimozione andata a buon fine."
    return dato

def Modifica(a):
    if a=="1":
        conn.send("Inserisci l'ID: ".encode())
        newID=conn.recv(1024).decode()
        newID="IDdip = "+"'"+str(newID)+"'"
        conn.send("Quale parametro vuoi cambiare:\n1 - ID \n2 - Nome\n3 - Cognome\n4 - Posizione lavorativa\n5 - Data di assunzione\n6 - Stipendio\n7 - Data di nascita\n8 - Telefono ".encode())
        risp=conn.recv(1024).decode()
        while int(risp) <= 0 or int(risp) >8 :
            conn.send("Quale parametro vuoi cambiare:\n1 - ID \n2 - Nome\n3 - Cognome\n4 - Posizione lavorativa\n5 - Data di assunzione\n6 - Stipendio\n7 - Data di nascita\n8 - Telefono".encode())
            risp=conn.recv(1024).decode()
        var=""
        a=""
        risp=int(risp)

        if risp==1:
            conn.send("Inserisci il nuovo ID: ".encode())
            var=str(conn.recv(1024).decode())

            a="IDdip = "+"'"+str(var)+"'"
        
        elif risp==2:
            conn.send("Inserisci il nuovo nome: ".encode())
            var=conn.recv(1024).decode()
            
            a="nome = "+"'"+var+"'"
        
        elif risp==3:
            conn.send("Inserisci il nuovo cognome: ".encode())
            var=conn.recv(1024).decode()
            
            a="cognome = "+"'"+var+"'"
        
        elif risp==4:
            conn.send("Inserisci la nuova posizione lavorativa: ".encode())
            var=conn.recv(1024).decode()
            
            a="posizione_lavorativa = "+"'"+var+"'"

        elif risp==5:
            conn.send("Inserisci la data di assunzione: ".encode())
            var=conn.recv(1024).decode()
            
            a="data_assunzione = "+"'"+var+"'"
        
        elif risp==6:
            conn.send("Inserisci il nuovo stipendio: ".encode())
            var=conn.recv(1024).decode()
            
            a="stipendio = "+"'"+var+"'"        
        
        elif risp==7:
            conn.send("Inserisci la data di nascita: ".encode())
            var=conn.recv(1024).decode()
            
            a="data_nascita = "+"'"+var+"'"
        
        elif risp==8:
            conn.send("Inserisci il nuovo numero di telefono: ".encode())
            var=str(conn.recv(1024).decode())
            while len(var)>10:
                conn.send("Inserisci il nuovo numero di telefono: ".encode())
                var=str(conn.recv(1024).decode())
            a="telefono = "+"'"+str(var)+"'"

        print(a)
        query = (f"UPDATE dipendenti SET {a} WHERE {newID}")
        print(query)
        cur.execute(query)
        cono.commit()
        dato = "\nAggiornamento andato a buon fine.\n"
        
    if a=="2":
        conn.send("Inserisci l'ID della zona: ".encode())
        idZon=conn.recv(1024).decode()
        idZon="IDdip= "+"'"+str(idZon)+"'"
        conn.send("Quale parametro vuoi cambiare: \n1 - ID  \n2 - Nome della zona\n3 - Numero clienti\n4 - Temperatura' ".encode())
        risp=conn.recv(1024).decode()
        while int(risp) <= 0 or int(risp) >8 :
            conn.send("Quale parametro vuoi cambiare: \n1 - ID  \n2 - Nome della zona\n3 - Numero clienti\n4 - Temperatura' ".encode())
            risp=conn.recv(1024).decode()
        var=""
        a=""
        risp=int(risp)
        
        if risp==1:
            conn.send("Inserisci il nuovo ID della zona: ".encode())
            var=str(conn.recv(1024).decode())

            a="IDzona = "+"'"+str(var)+"'"        
        elif risp==2:
            conn.send("Inserisci il nuovo nome della zona: ".encode())
            var=conn.recv(1024).decode()
            
            a="nome = "+"'"+var+"'"
        elif risp==3:
            conn.send("Inserisci il nuovo numero clienti: ".encode())
            a="n_clienti = "+"'"+str(var)+"'"
        elif risp==4:
            conn.send("Inserisci la nuova temperatura:  ".encode())
            var=conn.recv(1024).decode()
            
            a="temperatura = "+"'"+var+"'"

        print(a)
        query = (f"UPDATE zone_di_lavoro SET {a} WHERE {idZon}")
        print(query)
        cur.execute(query)
        cono.commit()
        dato = "Aggiornamento andato a buon fine."
    return dato

def Inserimento(a):
    if a=="1":

        conn.send("Inserisci il nome: ".encode())
        var=conn.recv(1024).decode()
        
        nome=str(var)
        conn.send("Inserisci il cognome: ".encode())
        var=conn.recv(1024).decode()
        
        cognome=str(var)
        conn.send("Inserisci il stipendio:".encode())
        var=conn.recv(1024).decode()
        
        stipendio=str(var)
        conn.send("Inserisci il numero di telefono: ".encode())
        var=str(conn.recv(1024).decode())
        while len(var)>10:
            conn.send("Inserisci il numero di telefono: ".encode())
            var=str(conn.recv(1024).decode())
        telefono=str(var)

        conn.send("Inserisci la nuova posizione lavorativa: ".encode())
        var=conn.recv(1024).decode()
        
        posizione_lavorativa=str(var)
        conn.send("Inserisci la data di assunzione: ".encode())
        var=conn.recv(1024).decode()
        
        d_assunzione=str(var)
        conn.send("Inserisci la data di nascita: ".encode())
        var=conn.recv(1024).decode()
        
        d_nascita=str(var)

        print(a)
        query = (f"INSERT INTO `dipendenti` (`nome`, `cognome`, `posizione_lavorativa`, `data_assunzione`, `stipendio`, `telefono`, `data_nascita`) VALUES ('{nome}', '{cognome}', '{posizione_lavorativa}', '{d_assunzione}', '{stipendio}', '{d_nascita}', '{telefono}')")
        print(query)
        cur.execute(query)
        cono.commit()
        dato = "Inserimento andato a buon fine."

    if a=="2":
        conn.send("Inserisci il nuovo nome della zona: ".encode())
        var=conn.recv(1024).decode()
        
        nome=str(var)
        conn.send("Inserisci il nuovo numero clienti: ".encode())
        var=conn.recv(1024).decode()
        
        n_clienti=str(var)
        conn.send("Inserisci la nuova temperatura:  ".encode())
        var=conn.recv(1024).decode()
        temperatura=str(var)
        
        print(a)
        query = (f"INSERT INTO `zone_di_lavoro` (`nome`, `n_clienti`, `temperatura`) VALUES ('{nome}', '{n_clienti}', '{temperatura}')")
        print(query)
        cur.execute(query)
        cono.commit()
        dato = "Inserimento andato a buon fine."
    return dato

HOST = ''
PORT = 50000 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)

print("In attesa di connessioni...")

conn, addr = s.accept()
print('Connected by', addr)

if __name__ == '__main__':
    conn.send("Benvenuto, inserisci password: ".encode())
    data = conn.recv(1024).decode()
    
    i=0
    while data != pw:
        i+=1
        conn.send(f"Password inserita sbagliata, reinserisci: ".encode())
        data = conn.recv(1024).decode()
        if i == 3: conn.send("STOP".encode())

    while True:
        conn.send("\nOpzioni: \n1)Inserimento \n2)Modifica \n3)Leggere \n4)Elimina \n5)Uscire".encode())
        data = conn.recv(1024).decode()
        
        print(data)
        scelta=data
        if(scelta=="5"):
            conn.send("5".encode())
            conn.close()
            sys.exit()
        elif(scelta=="3"):
            conn.send("\n1)Dipendeneti \n2)Zone di lavoro:".encode())
            data = conn.recv(1024).decode()
                        
            dato_query = Lettura(data)

            a="\n--------------------------------\n"
            for j in range (0,len(dato_query)):
                for i in range (0, len(dato_query[j])):
                    a=a+str(dato_query[j][i])+"\n"
                a=a+"--------------------------------\n"
        
            print(dato_query)
            conn.send(a.encode())
        elif(scelta=="4"):
                conn.send("\n1)Dipendeneti \n2)Zone di lavoro:  ".encode())
                data = conn.recv(1024).decode()
                
                risposta=Elimina(data)
                print(risposta)
                conn.send(risposta.encode())

        elif(scelta=="2"):
                conn.send("\n1)Dipendeneti \n2)Zone di lavoro:   ".encode())
                data = conn.recv(1024).decode()
                
                risposta=Modifica(data)
                print(risposta)
                conn.send(risposta.encode())

        elif(scelta=="1"):
                conn.send("\n1)Dipendeneti \n2)Zone di lavoro:   ".encode())
                data = conn.recv(1024).decode()
                
                risposta=Inserimento(data)
                print(risposta)
                conn.send(risposta.encode())