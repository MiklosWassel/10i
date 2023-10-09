'''
print("Kérem a neved:",end=" ")
nev = input()

print("Szia "+nev)

nev = input("Kérem a neved2: ")
print("Szia "+nev+"!")

szam = input("Kérek egy egész számot 10 és 100 között: ")
print(szam)
print(szam*2)
print(type(szam))

szam = float(input("Kérek egy egész számot 0 és 1 között: "))
print(szam)
print(szam*2)
print(type(szam))
'''
'''
szam = int(input("Kérek egy egész számot 1 és 100 között: "))

# + - / * ** % //

maradek = szam % 2 
if maradek == 0 :
    print("Páros")
else: 
    print("Páratlan")
'''
'''
szam = int(input("Kérek egy egész számot 1 és 100 között: "))
 
maradek = szam % 3
if maradek == 0 :
    print("Hárommal osztható")
else: 
    print("Hárommal nem osztható")

'''
'''
szam = int(input("Kérek egy egész számot 1 és 100 között: "))

pozitiv = szam > 0
negativ = szam < 0
nulla = szam == 0

# print(type(pozitiv),pozitiv)

if pozitiv :
    print("pozitiv")
if negativ :
    print("negativ")
if nulla :
    print("nulla")

if szam > 0 :
    print("pozitiv")
else:
    if szam < 0 :
    print("negativ")
     
    print("nulla")
'''
'''
szam = int(input("Kérek egy pozitiv egész számot: "))
maradek2 = szam % 2
maradek3 = szam % 3


if maradek2 == 0 and maradek3 != 0 :
    print("Kettővel osztható")

if maradek3 == 0 and maradek2 != 0 :
    print("Hárommal osztható")

if maradek3 == 0 and maradek2 == 0 :
        print("Hattal osztható")


if maradek2 == 0 and maradek3 != 0 :
    print("Kettővel osztható")

elif maradek3 == 0 and maradek2 != 0 :
    print("Hárommal osztható")

elif maradek3 == 0 and maradek2 == 0 :
        print("Hattal osztható")

print("-"*10)

if maradek2 or maradek3 == 0 :
    print("kettővel vagy hárommal osztható")
else:
    print("Se kettővel vagy hárommal osztható")
'''
if 1 :
    print(1)
if 0 :
     print(0)
