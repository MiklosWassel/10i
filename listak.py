#lista = set()
lista = []
print(type(lista))
lista = list()
print(type(lista))

lista = [1,2,3,4,5]
print(len(lista))
print(sum(lista))

lista.append(10)
print(lista)

lista.append("Alma")
print(lista)
print(len(lista))
#print(sum(lista))


lista2 = ['a','b','c']
lista.append(lista2)
print(lista)
print(len(lista))

#lista.clear() üres listát kiüríti a listát

'''
l = lista
l.append(100)
print(lista)
a = 10
b = a
b = 11
print(a)
'''

l = lista.copy()
l.append(100)
print(l,lista,sep="\n")

print(lista.count(4))
print("Almaa".count('a'))

print(lista.index(5))

lista.insert(3,"szilva") # berak egy megadott betűt vagy számot az adot helyre
print(lista)

#print(lista.pop(-1)) # elvesz és visszaadja az indexet
print(lista.pop(len(lista)-1))
print(lista)

lista.remove("Alma") # kivesz és nem add vissza értéket
print(lista)

lista.append(5)
print(lista)
lista.remove(5)
print(lista)

print(lista[4])
lista[4] = 20
print(lista)

lista.reverse() # megfordítja a listát
print(lista)

lista.sort() # helyre rakja
print(lista)

mondat = "Voluptate Lorem cillum voluptate sit culpa fugiat sunt pariatur labore."
