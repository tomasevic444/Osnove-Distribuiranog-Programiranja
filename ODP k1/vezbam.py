class Trougao:
    boja = "plava"
    a=b=1
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

trougao2 = Trougao(2,4,5)
    
trougao = Trougao()
print(trougao.boja)

class Trougao:
    boja = "plava"
    a= b= 1
    
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
        return "Trougao, boja:{self.boja}, stranice : {self.a},{self.b}"
    def obim(self):
        return self.a + self.b+self.c


f = open("demo.txt","r")
print(f.read())

