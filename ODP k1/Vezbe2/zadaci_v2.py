# Kontrola toka programa (str. 31)

# 1. Tražiti od korisnika da unese neki broj. 
# Ukoliko je taj broj manji od 0, ispiši “Uneli ste
# negativni broj.”

def zadatak_kontrola_toka_1():
   broj = float(input("Unesite neki broj: "))
   if broj<0 : print("Uneli ste negativan broj")

# 2. Tražiti od korisnika da unese dva broja i 
# sačuvati ih u promenljive a i b. 
# Skraćenim zapisom ifelse strukture ispisati 
# onaj broj koji je veći, odnosno poruku da su 
# jednaki ukoliko je to slučaj.

def zadatak_kontrola_toka_2():
   a = int(input("Unesite prvi broj: "))
   b = int(input("Unesite drugi broj: "))

   # Prvi način
   if a == b : print("Brojevi su jednaki")
   elif a>b : print("Prvi broj je veci od drugog")
   elif b>a : print("Drugi broj je veci od prvog")

   # Drugi način
   print("Prvi broj je veci od drugog") if a>b else print ("Brojevi su jednaki") if a == b else print("Drugi broj je veci od prvog") 

# 3. Kreirati listu povrća, a zatim proveriti da li se “krompir” 
# nalazi u listi. Ukoliko se nalazi,
# ispisati odgovarajuću poruku, a ukoliko se ne nalazi, 
# proveriti da li se “grasak” nalazi u listu.
# Opet, ukoliko se nalazi, ispisati odgovarajuću poruku,
# a ukoliko se ne nalazi ispisati “Vreme je za nabavku.”

def zadatak_kontrola_toka_3() :
   listaPovrca = ["paradajz", "grasak", "boranija", "luk"]
   if "krompir" not in listaPovrca : 
      print("Krompir se ne nalazi u listi")
      if "grasak" in listaPovrca :
         print("Grasak se nalazi u listi")
      else : 
         print("Vreme je za nabavku")
   else :
      print("Krompir se nalazi u listi")


# 4. Kreirati listu brojeva i pomoću for petlje ispisati svaki od njih.
def zadatak_kontrola_toka_4():
   brojevi = [1,3,4,6,7,9,7,8,12,43]
   for broj in brojevi : print(broj)

# 5. Kreirati torku logičkih vrednosti i pomoću for petlje ispisati svaku od njih.

def zadatak_kontrola_toka_5():
   torka = (True, False, True, False)
   for clanTorke in torka: print(clanTorke)

# 6. Kreirati skup stringova i pomoću for petlje ispisati svaki od njih.

def zadatak_kontrola_toka_6():
   skup = {"nije", "tesko", "biti", "fin"}
   for rec in skup : print(rec)

# 7. Kreirati proizvoljni rečnik i pomoću for petlje ispisati sve ključeve.
def zadatak_kontrola_toka_7():
   recnik = dict(ime = "Petar", prezime ="Mitic", nadimak="Pero", zanimanje ="glumac")
   for kljuc in recnik.keys(): 
      print(kljuc)

# 8. Data je lista: lista = ["jabuke", "banane", "kivi", "mandarine", "grozdje", "mango"]. Pomoću
# for petlje ispisivati element po element. Ukoliko se „kivi“ nalazi u listi, preskočiti ga i nastaviti
# ispis od sledećeg elementa, a ukoliko se „grozdje“ nalazi u listi prekinuti izvršavanje petlje.
def zadatak_kontrola_toka_8():
   lista = ["jabuke", "banane", "kivi", "mandarine", "grozdje", "mango"]
   for voce in lista :
      if voce == "kivi" : continue
      if voce == "grozdje" : break
      print(voce)

# 9. Data je promenljiva i = 5. Ispisivati njenu vrednost u while petlji dokle god je ona manja ili
# jednaka 10.
def zadatak_kontrola_toka_9():
   i=5
   while i<=10 :
      print(i)
      i+=1
    
# 10. Data je promenljiva i = 1. Ispisivati njenu vrednost u while petlji dokle god je ona manja od 6,
# a kada prestane da bude manja, ispisati „Vrednost promenljive i više nije manja od 6“.
def zadatak_kontrola_toka_10():
   i=1
   while i<6 :
      print(i)
      i+=1
   else : print (("Vrednost promenljive je {}, više nije manja od 6").format(i))

def zadatak_kontrola_toka(broj_zadatka):
   if(broj_zadatka == 1): zadatak_kontrola_toka_1()
   elif(broj_zadatka == 2): zadatak_kontrola_toka_2()
   elif(broj_zadatka == 3): zadatak_kontrola_toka_3()
   elif(broj_zadatka == 4): zadatak_kontrola_toka_4()
   elif(broj_zadatka == 5): zadatak_kontrola_toka_5()
   elif(broj_zadatka == 6): zadatak_kontrola_toka_6()
   elif(broj_zadatka == 7): zadatak_kontrola_toka_7()
   elif(broj_zadatka == 8): zadatak_kontrola_toka_8()
   elif(broj_zadatka == 9): zadatak_kontrola_toka_9()
   elif(broj_zadatka == 10): zadatak_kontrola_toka_10()
   else : print('Morate uneti broj od 1 do 10')


# Obrada izuzetaka i funkcije (str. 36)

# Zadatak 1
# Napisati funkciju koja prihvata listu kao parametar i 
# menja je tako što na prvo mesto smešta najveći element,
# a na poslednje najmanji
def funkcija1(lista):
   maksi = max(lista)
   lista.remove(maksi)
   mini = min(lista) 
   lista.remove(mini)
   lista.insert(0, maksi)
   lista.append(mini)

#DRUGI NACIN
lista = [2, 15, 5, 28, 9, 30, 4]
def funkcija2(lista):
   maksi = max(lista)
   mini = min(lista) 
   lista[0] = maksi
   lista[-1] = mini
 
def zadatak_funkcije_1():   
   lista = [2, 15, 5, 28, 9, 30, 4]
   print("Vrednosti pre zamene => ", lista)
   funkcija1(lista)
   print("Vrednosti nakon zamene => ", lista)
   lista = [2, 15, 5, 28, 9, 30, 4]
   funkcija2(lista)
   print("Vrednosti nakon zamene => ", lista)

# Zadatak 2
# Napisati funkciju koja može da prima promenljiv broj parametara.
# Ukoliko je prosleđeno više od tri parametra, iz funkcije vratiti njihovu sumu,
# a u suprotnom vratiti njihov proizvod.
# Pozvati funkciju sa 2 i sa 4 parametra.
def funkcija_za_racunanje(*args):
   if len(args) == 0:
      raise Exception("Potrebno je proslediti barem jedan parametar!")
   if len(args) > 3:
    return sum(args)
   else:
      prod = 1
      for arg in args:
         prod *=arg
      return prod
   
def zadatak_funkcije_2():   
   print("Izuzetak () => ", funkcija_za_racunanje())
   print("Proizvod (2,3) => ", funkcija_za_racunanje(2, 3))
   print("Suma (2, 3, 7, 13) => ",funkcija_za_racunanje(2, 3, 7, 13))

# Zadatak 3
# 3.	Napisati funkciju koja prima dva celobrojna parametra i pokušava da ih podeli, 
# te da vrati količnik. Ukoliko je za delilac prosleđena nula, 
# odgovarajući izuzetak će biti uhvaćen i obrađen.
def podeli(a: int, b: int):
   try:
      return a/b
   except ZeroDivisionError as zde:
      print("Greska:", zde)
      
def zadatak_funkcije_3():   
   print("10/3 =", podeli(10, 3))
   print("10/0 =", podeli(10, 0))

# Zadatak 4
# Sortirati datu listu numerički:
def zadatak_funkcije_4():   
   lista = ["10", "2", "19", "0", "-1", "-20", "5"]
   print("Sortirana lista => ", sorted(lista, key=lambda x: int(x)))

# Zadatak 5
# Napisati sopstvenu funkciju za filtriranje, 
# koja kao parametre prihvata listu i anonimnu funkciju, 
# kojom je određen uslov po kome se filtrira.
# Pomoću ove funkcije iz date liste izdvojiti sve parne brojeve, 
# a zatim i sve negativne.
def filter_funkcija(lista, uslov):
   rezultat = []
   for element in lista:
      if uslov(element):
         rezultat.append(element)
   return rezultat

def zadatak_funkcije_5():   
   lista = [2, 15, -5, 28, 9, -30, 4, -1]
   print("Parni brojevi => ", filter_funkcija(lista, lambda x: x%2==0))
   print("Negativni brojevi => ",filter_funkcija(lista, lambda x: x < 0))

   # Rešenje preko ugrađene funkcije filter
   lista = list(filter(lambda x: x<0, lista))
   print("Negativni brojevi(ugradjeni filter) => ", lista)

# Zadatak 6
# Uvećati svaki element date liste za 10, ali tako da sve vrednosti ostanu stringovi.
# Koristiti ugrađenu funkciju map i lambda funkciju.
def zadatak_funkcije_6():   
   lista = ["10", "2", "19", "0", "-1", "-20", "5"]
   print(lista, " <= Pocetne vrednosti")
   print(list(map(lambda x: str(int(x) + 10), lista)), " <= Vrednosti uvecane za 10", )

def zadatak_funkcije(broj_zadatka):
   if(broj_zadatka == 1): zadatak_funkcije_1()
   elif(broj_zadatka == 2): zadatak_funkcije_2()
   elif(broj_zadatka == 3): zadatak_funkcije_3()
   elif(broj_zadatka == 4): zadatak_funkcije_4()
   elif(broj_zadatka == 5): zadatak_funkcije_5()
   elif(broj_zadatka == 6): zadatak_funkcije_6()
   else : print("Morate uneti broj od 1 do 6")

while True:
   broj_zadatka = int(input("Unesite broj zadatka: "))
   try:
      zadatak_kontrola_toka(broj_zadatka)
      # zadatak_funkcije(broj_zadatka)
   except Exception as e:
      print("Greska:", e)
  