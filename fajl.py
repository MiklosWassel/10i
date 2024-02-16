fajl = open("ub2017egyeni.txt") # megnyit egy fájlt

#print(fajl.read())  #vissza add egy str-et

#print(fajl.readline()) # kiír afájlból egy sort annyiszor ahányszor megvan adva 
#print(fajl.readline())

#print(fajl.readlines()) # listát add vissza
#print("*"*10)
#print(fajl.readlines())

versenyzok = list()
fejlec = fajl.readline()
for sor in fajl:
    #print(sor.replace("\n","").split(";"))
    listasor = sor.replace("\n","").split(";")
    #print(listasor[0])
    versenyzo = {"nev":listasor[0],"Rajtszam":listasor[1],"kategoria":listasor[2],"Versenyido":listasor[3],"TavSzazalek":int(listasor[4])}
    #print(versenyzo)
#print(fajl.readline()) nem lehet már bezárt fájlba szerkezteni
    versenyzok.append(versenyzo)
fajl.close() # Bezárja fájlt

#print(versenyzok)

f = open("versenyzok.txt","w")

for v in versenyzok:
    #print(v["nev"])
    f.write(v["nev"])
    f.write("\n")
f.close()

teljes = 0
for v in versenyzok:
    if v["TavSzazalek"] == 100:
        teljes += 1
print(teljes)

minimum = 100
rovid =""
for v in versenyzok:
    if v["TavSzazalek"] < minimum :
        minimum = v["TavSzazalek"]
        rovid = v["nev"]
print(rovid,minimum)
