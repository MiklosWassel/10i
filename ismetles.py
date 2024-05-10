'''
lista = list()
ismet = True
while ismet:
    beker = input("Kérek számokat: ")
    if beker == "":
      ismet = False
    else:
        lista.append(beker)
print(lista)

db = 0
for e in lista:
    if e % 3 == 0:
        db += 1

print(db)


def paros(lista):
    plista = list()
    return li
print(minimum(x))

def maximum(v):
    b = v[0]
    for li2 in v:
        if li2 > v:
            li2 = v
    return v
print(maximum(v))

lista =[1,2,33,-6,7]

def osszegzes(li3):
    ossz = 0
    for v in li3:
        ossz += v
    return ossz
print(osszeg(lista))


def kicsi(li,db):  # db. -ik legkissebb vissza
    return sorted(lista)[db-1]

print(sorted(lista))
print(lista)
'''
def nagy(li,db):  # db. -ik legkissebb vissza
    return sorted(lista,reverse=True) [db-1]
print(nagy(lista,2))
 # sorted = lista rendezet sorrendbe
'''
lista.remove(-6)
print(lista)
'''

def kicsi2(li,db):
    mi = min(li)
    if db == 1:
        return mi
    else:
        li.remove(mi)
        db += -1
        licsi2(li,db)
print(kicsi2(lista,1))
print(lista)
