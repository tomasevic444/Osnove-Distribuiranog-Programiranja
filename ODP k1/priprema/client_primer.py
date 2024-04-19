import pickle,socket,json
from profesor import Profesor
from datetime import date

klijent = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

klijent.connect(('localhost',8081))

print("\nKonekcija uspostavljena")

def prikupi_informacije_za_profesora():
        jmbg = input("JMBG profesora -> ")
        ime = input("Ime profesora -> ")
        prezime = input("Prezime profesora -> ")
        godina,mesec,dan = input("Unesite datum u formatu YYYY-MM-DD -> ").split('-')
        profesor = Profesor(jmbg,ime,prezime,date(int(godina),int(mesec),int(dan)),[])
        print(profesor.jmbg)
        return pickle.dumps(profesor)

def prikupi_jmbg_za_profesora():
        jmbg = input("JMBG profesora -> ")
        return jmbg.encode()

def ispisi_profesora(poruka):
        print("\n---------------------------------------------------")
        try:
                profesor = pickle.loads(poruka)
                print(profesor)
        except:
                print(poruka.decode())
        print("---------------------------------------------------\n")

def prikupi_predmete_za_profesora():
        predmeti = input("Unesite predmete (odvojte ih zarezom): ").split(',')
        return pickle.dumps(predmeti)

def ispisi_sve_profesore(poruka):
        profesori = pickle.loads(poruka)
        print("\n******************************************")
        for profesor in profesori.values():
                print(profesor)
        print("******************************************\n")

def ispis(poruka):
        print("\n---------------------------------------------------")
        print(poruka)
        print("---------------------------------------------------\n")

while True:
        operacija = input("Unesite opciju: \n 1.Dodaj profesora \n 2.Izmeni profesora\n 3.Obrisi profesora\n 4.Ipisi profesora \n 5.Dodaj predmete profesoru\n 6.Izlistaj predmete koje predaje profesor\n 7.Ispisi sve profesore \n 8.Uvezi profesore iz json fajla\n 9.Izvezi sve profesore sa vise od 20 godina staza\n")
        if not operacija : break
        if operacija == "1":
                klijent.send(("ADD").encode())
                klijent.send(prikupi_informacije_za_profesora())
                ispis(klijent.recv(1024).decode())
        elif operacija == "2":
                klijent.send(("UPDATE").encode())
                klijent.send(prikupi_informacije_za_profesora())
                ispis(klijent.recv(1024).decode())
                
        elif operacija == "3":
                klijent.send(("DELETE").encode())
                klijent.send(prikupi_jmbg_za_profesora())
                ispis(klijent.recv(1024).decode())
        elif operacija == "4":
                klijent.send(("READ").encode())
                klijent.send(prikupi_jmbg_za_profesora())
                ispisi_profesora(klijent.recv(1024))
        elif operacija == "5":
                klijent.send(("ADD_SUBJ").encode())
                klijent.send(prikupi_jmbg_za_profesora())
                klijent.send(prikupi_predmete_za_profesora())
                ispis(klijent.recv(1024).decode())
        elif operacija == "6":
                klijent.send(("READ_SUBJ").encode())
                klijent.send(prikupi_jmbg_za_profesora())
                ispis(klijent.recv(1024).decode())
        elif operacija == "7":
                klijent.send(("READ_ALL").encode())
                ispisi_sve_profesore(klijent.recv(1024))
        elif operacija == "8":
                klijent.send(("UVOZ").encode())
                ispis(klijent.recv(1024).decode())
        elif operacija == "9":
                klijent.send(("STAZ").encode())
                ispis(klijent.recv(1024).decode())
        else:
                print("\nMolimo unesite validnu opciju\n")
                continue

print("Konekcija prekinuta")
klijent.close()