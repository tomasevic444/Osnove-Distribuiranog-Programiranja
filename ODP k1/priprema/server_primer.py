import pickle,socket,json
from profesor import Profesor
from datetime import date

profesori = {}

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('localhost',8081))

server.listen()
print("\nServer je otvoren")

kanal, adresa = server.accept()

print(f"\nKonektovano na adresi: {adresa}")

def dodaj_profesora(poruka):
        profesor = pickle.loads(poruka)
        if profesor.jmbg not in profesori:
                odgovor = f"Profesor sa JMBG-om: {profesor.jmbg} je uspesno dodat u bazu"
                profesori[profesor.jmbg] = profesor
        else:
                odgovor = f"Profesor sa JMBG-om: {profesor.jmbg} vec postoji u bazi"
        return odgovor.encode()

def izmeni_profesora(poruka):
        profesor = pickle.loads(poruka)
        if profesor.jmbg in profesori:
                odgovor = f"Profesor sa JMBG-om: {profesor.jmbg} je uspesno izmenjen"
                profesori[profesor.jmbg] = profesor
        else:
                odgovor = f"Profesor sa JMBG-om: {profesor.jmbg} ne postoji u bazi"
        return odgovor.encode()

def obrisi_profesora(jmbg):
        if jmbg not in profesori:
                odgovor = f"Profesor sa JMBG-om: {jmbg} ne postoji u bazi"
        else:
                odgovor = f"Profesor sa JMBG-om: {jmbg} je uspesno obrisan"
                del profesori[jmbg]
        return odgovor.encode()

def pronadji_profesora(jmbg):
        if jmbg not in profesori:
                odgovor = f"Profesor sa JMBG-om: {jmbg} ne postoji u bazi"
                return odgovor.encode()
        else:
                odgovor = pickle.dumps(profesori[jmbg])
                return odgovor
                
def dodaj_predmete(jmbg,podaci):
        if jmbg in profesori:
                pr = pickle.loads(podaci)
                profesori[jmbg].predmeti.extend(pr)
                odgovor = f"Profesoru sa JMBG-om: {jmbg} su uspesno dodati predmeti"
        else:
                 odgovor = f"Profesor sa JMBG-om: {jmbg} ne postoji u bazi"
        return odgovor.encode()

def izvuci_predmete(jmbg):
        if jmbg in profesori:
                predmeti_lista = profesori[jmbg].predmeti
                predmeti_lista.sort()
                odgovor = "Predmeti: "
                for pr in predmeti_lista:
                        odgovor += f"{pr}, "
        else:
                 odgovor = f"Profesor sa JMBG-om: {jmbg} ne postoji u bazi"
        return odgovor.encode()

def svi_profesori():
        return pickle.dumps(profesori)

def uvoz():
        fajl = open("profesori.json","r")
        data = json.load(fajl)
        lista = [Profesor(profesor["jmbg"],profesor["ime"],profesor["prezime"],profesor["datum"],profesor["predmeti"])for profesor in data]
        for it in lista:
                datum_string = it.datum.split('-')
                godina = datum_string[0]
                mesec = datum_string[1]
                dan = datum_string[2]
                it.datum = date(int(godina),int(mesec),int(dan))

        return lista

def ispisi_staz():
        fajl = open("godineStaza.txt","w")
        for prof in profesori.values():
                staz = 2024 - int(prof.datum.year)
                if staz >= 20:
                        fajl.write(prof.__str__() + f", staz: {staz} godina\n")
                
        fajl.close()

while True:
        opcija = kanal.recv(1024).decode()
        if not opcija : break
        if opcija == "ADD":
                odgovor = dodaj_profesora(kanal.recv(1024))
        elif opcija == "UPDATE":
                odgovor = izmeni_profesora(kanal.recv(1024))
        elif opcija == "DELETE":
                odgovor = obrisi_profesora(kanal.recv(1024).decode())
        elif opcija == "READ":
                odgovor = pronadji_profesora(kanal.recv(1024).decode())
        elif opcija == "ADD_SUBJ":
                jmbg = kanal.recv(1024).decode()
                podaci = kanal.recv(1024)
                odgovor = dodaj_predmete(jmbg,podaci)
        elif opcija == "READ_SUBJ":
                odgovor = izvuci_predmete(kanal.recv(1024).decode())
        elif opcija == "READ_ALL":
                odgovor = svi_profesori()
        elif opcija == "UVOZ":
                lista = uvoz()
                for prof in lista:
                        profesori[prof.jmbg] = prof
                odgovor = "Uspesno uvezeni profesori".encode()
        elif opcija == "STAZ":
                ispisi_staz()
                odgovor = "Staz je uspesno izvezen u datoteku \"godineStaza.txt\"".encode()
        kanal.send(odgovor)

print("Server zatvoren")
server.close()

