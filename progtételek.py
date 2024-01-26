
import random

def listaGen(darab,tol,ig):

    lista = list()
    for i in range(darab):
        lista.append(random.randint(tol,ig))
    return lista

lista = listaGen(10,1,45)
print(lista)
lista = listaGen(10,50,200)
print(lista)

# megszámolás
def megszamol(listam):
    db = 0
    for elem in listam:
        if elem > 50:
            db += 1
    return db
print(f"{megszamol(lista)} Volt 50-nél nagyobb")

# eldöntés
def eldontes(lista):
    volt = False
    for elem in lista:
        if elem > 90:
            volt = True
    return volt

if eldontes:
    print("volt")
else:
    print("Nem volt 90-nél nagyobb")

# eldöntés v2
volt = False
for elem in lista:
    if elem > 90:
        votl = True
        break
if volt:
    print("volt")
else:
    print("Nem volt 90-nél nagyobb")

# eldöntés v3
volt = False
i = 0
while not volt and i < len(lista):
    # print(lista[i])
    if lista[i] > 90:
        volt = True
    i += 1

if volt:
    print("volt")
else:
    print("Nem volt 90-nél nagyobb")

# összegzés    
osszeg = 0

def osszegzes(l):
    osszeg = 0
    for elem in l:
        osszeg += elem
    return osszeg

print(osszegzes(lista))
print(osszegzes([1,2,3,4,4]))
print(osszegzes({1,2,3,4,4}))
print(osszegzes((1,2,3,4,4)))

print(sum(lista))

# átlag pl: sum(lista)/len(lista)
def atlag(l):
    db = 0
    osszeg = 0
    for elem in l:
        osszeg += elem
        db += 1
    return osszeg / db
print(atlag([2,4]))
print(atlag(lista))