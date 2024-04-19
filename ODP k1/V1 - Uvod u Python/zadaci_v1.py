# Operatori (str. 12)
def taskOne():
    # Zadatak 1
    # Dodeliti vrednost sledećeg izraza promenljivoj x: 5^2 + 3/4

    x = 5**2 + 3/4
    print("Vrednost izraza je", x)

    # Zadatak 2
    # Neka je a = 17, a b = 3. Odrediti količnik i ostatak pri deljenju a sa b.
    # Zapisati ih u promenljive kolicnik i ostatak

    a, b = 17, 3
    kolicnik = a / b
    ostatak = a % b
    print("Kolicnik je ", kolicnik)
    print("Ostatak pri deljenju je ", ostatak)

    # Zadatak 3 
    # Celobrojno podeliti kolicnik sa 2, a zatim rezultat uvećati tri puta

    rezultat = kolicnik//2
    rezultat*=3
    print("Rezultat je ", rezultat)

    # Zadatak 4
    # Napisati logički izraz koji će vratiti tačno 
    # ukoliko se a nalazi između 5 i 10, uključujući ih

    a = 10
    izraz = a>=5 and a<=10
    print(izraz)

    # Zadatak 5
    # Napisati logički izraz koji će vratiti 
    # tačno ukoliko je a strogo manje od –10 ili strogo veće od 10.

    a = -11
    izraz = a<-10 or a>10
    print(izraz)

    # Zadatak 6
    # Negirati logičke izraze iz prethodna dva zadatka

    a = 10
    izraz = not(a>=5 and a<=10)
    print(izraz)

    a = -11
    izraz = not(a<-10 or a>10)
    print(izraz)

# Tipovi podataka, interakcija sa korisnikom i 
# rad sa stringovima (str. 18)
def taskTwo():
    # Zadatak 1
    # Tražiti od korisnika da unese dva realna broja, sabrati ih i ispisati rezultat na ekran.

    r1 = float(input("Unesite prvi realan broj :"))
    r2 = float(input("Unesite drugi realan broj :"))
    rezultat = r1 + r2
    print("Rezultat sabiranja je ", rezultat)

    # Zadatak 2
    # Tražiti od korisnika da unese tri cela broja, koji redom predstavljaju 
    # dan, mesec i godinu, a zatim ih ispisati na ekran u sledećem formatu: dd/mm/yyyy

    dan = int(input("Unesite dan :"))
    mesec = int(input("Unesite mesec :"))
    godine = int(input("Unesite godinu :"))
    print(dan, mesec, godine, sep='/') 

    # Zadatak 3
    # Tražiti od korisnika da unese neki tekst, prebaciti ga u mala slova, 
    # obrisati sve bele karaktere sa oba kraja tog teksta 
    # i podeliti ga po razmaku.

    tekst = input("Unestite tekst: ")
    lista = tekst.strip().lower().split(" ")
    print(lista)

    # Zadatak 4
    # Tražiti od korisnika da unese neki tekst i zameniti 
    # svaku pojavu reči ’cao’ sa ’zdravo’.

    tekst = input("Unestite tekst: ")
    print(tekst.replace("cao", "zdravo")) 

    # Zadatak 5
    # Tražiti od korisnika da unese neki tekst i 
    # napisati sledeče logičke izraze:
    # a. ’je’ se nalazi u tekstu
    # b. ’sam’ se ne nalazi u tekstu
    # c. Prvo slovo je ’A’
    # d. Dužina teksta je različita od nule

    tekst = input("Unestite tekst: ")

    if 'je' in tekst:
        print ("je se nalazi u tekstu")
    if 'sam' not in tekst:
        print ("sam se ne nalazi u tekstu")
    if tekst[0]=='A':    
        print("Tekst pocinje slovom A")
    if len(tekst)>0:
        print("Tekst ima vise od 0 karaktera")

    # Zadatak 6
    # Tražiti od korisnika da unese ime, prezime i godine, odvojene zarezom. 
    # Svaku vrednost sačuvati u posebnu promenljivu i zatim ih ispisati u 
    # sledećem formatu: „Marko Marković ima 20 godina.“

    tekst = input("Unestite ime, prezime i koliko imate godina sve odvojeno zarezom: ")
    ime, prezime, godine = tekst.split(',')
    ime = ime.strip()
    prezime = prezime.strip()
    godine = godine.strip()
    print (("{} {} ima {} godina.").format(ime, prezime, godine))

# Liste i rečnici (str. 25)
def taskThree():
    # 1. Data je lista:
    lista = ["jabuke", "banane", "kivi", "mandarine", "grozdje", "mango"]

    # a) Ispiši drugi element.
    print(lista[1])
    # b) Promeni treći element na “kupine”.
    lista[2] = "kupine"
    print(lista[2])
    print(lista)
    # c) Dodaj vrednost “narandže” na kraj liste.
    lista.append("narandze")
    print(lista)
    # d) Ubaci vrednost “limun” na indeks 2.
    lista.insert(2,"limun")
    print(lista)
    # e) Ukloni vrednost “mandarine” iz liste.
    lista.remove("mandarine")
    print(lista)
    # f) Ispiši elemente od drugog zaključno sa petim.
    print(lista[1:5])
    # g) Ispiši poslednji element liste.
    print("Poslednji element", lista[-1])
    # h) Ispiši dužinu liste.
    print(len(lista))
    # i) Sortiraj listu.
    lista.sort()
    print(lista)
    # j) Obriši promenljivu lista.
    del lista

    # 2. Dat je rečnik:
    recnik = {
    "marka": "Ford",
    "model": "Mustang",
    "godina": 1964
    }
    print(recnik)

    # a) Ispiši vrednost pod ključem “model” na oba načina.
    print(recnik["marka"])
    print(recnik.get("marka"))
    # b) Promeni vrednost pod ključem “godina” na 2003.
    recnik["godina"] = 2003
    recnik.update({"godina": 2003})
    print(recnik)
    # c) Dodaj novi par ključ- vrednost koji će definisati da je boja žuta.
    recnik["boja"] = "zuta"
    print(recnik)
    # d) Obrisati ključ “marka” iz rečnika.
    # recnik.pop("marka")
    del recnik["marka"]
    print(recnik)
    # e) Obrisati sve parove ključ-vrednost iz rečnika.
    recnik.clear()
    print(recnik)

# Dodatni rad: Torke (str. 28) 
# Dodatni rad: Skupovi (str. 30)

def taskFour():
    torka = ("jabuke", "banane", "kivi", "mandarine", "grozdje", "mango")

    # 1. Ispiši prva četiri elementa.
    print(torka[:4])
    # 2. Ispiši poslednja dva elementa.
    print(torka[-2:])
    # 3. Kreiraj promenljivu za vrednost “mango” 
    # i promenljivu koja će sadržati sve ostale vrednosti torke.
    (*sveOstalo, mango) = torka
    print(sveOstalo)
    print(mango)

    skup = {"jabuke", "banane", "kivi", "mandarine", "grozdje", "mango"}

    # 1. Dodaj vrednost “narandze”.
    skup.add("narandze")
    print(skup)
    # 2. Dodaj skupu sledeću listu: [“visnje”, “jagode”, “maline”, “kupine”].
    lista = ["visnje", "jagode", "maline", "kupine"] 
    skup.update(lista)
    print(skup)
    # 3. Tražiti od korisnika da unese vrednost koju želi da ukloni iz skupa. 
    # Brisanje izvršiti tako da program ne izbaci grešku ukoliko je korisnik 
    # uneo nepostojeću vrednost.
    rec = input("Unesite vrednost koju zelite da obrisete iz skupa koji je gore naveden: ")
    skup.discard(rec)
    print(skup) 
   
#Pozivanje svih taskova
# taskOne()
taskTwo()
# taskThree()
# taskFour()