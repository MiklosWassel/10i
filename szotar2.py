mondat = "Deserunt nisi nulla minim labore."

betuk = dict()
#mondat = mondat.lower()
#mondat = mondat.replace(".","")
mondat = mondat.lower().replace(".","").replace(" ","")
#print(mondat)

for k in mondat:
    #print(k)
    #print(betuk.get(k))
    if betuk.get(k) == None:
        betuk.update({k:1})
    else:
        betuk.update({k:betuk.get(k)+1})
print(betuk)
'''
betuk.clear()
for k in mondat:
    db = betuk.get(k)
    if db == None:
        betuk.update({k:1})
    else:
        betuk.update({k:db + 1})
print(betuk)

print(betuk.items())
for kulcs,elem in betuk.items():
    print(kulcs,elem,end="; ")
print()

#betuk.pop('v') eltünteti az adott elemet
#print(betuk)


#print(betuk.popitem())  elevesz két elemet a végéről és tuple-be visszaadja
#print(betuk.popitem())

#betuk.setdefault('1','nincs') #berakja az adott kulcsot és beteszi a végére
#print(betuk)

#karakter = input("Kérek egy betüt: ")
#for betu in betuk:
#    if betu :
 #       print("Benne van a mondatba")
  #  else:
   #     print("Nincs benne")

karakter = input("Kérek egy betüt: ")
if betuk.get(karakter) == None:
    print("A "+karakter+" nem szerepel a mondatba")
else:
    print("A "+karakter+" "+str(betuk.get(karakter))+" alkalommal szerepel a mondatba")

#print('d' in betuk.keys())
#rint('D' in betuk.keys())
valid ="asqdwerfgtzhujkiolmnbvcxyp"
print(sorted(valid))

while True: # még hibás
    karakter = input("Kérek az angól ABC-ből egy betüt: ")
    if karakter in valid:
        break

ismeteld = True
while ismeteld:
    karakter = input("Kérek az angól ABC-ből egy betüt: ").lower()
    
    if karakter in valid:
        ismeteld = False
    else:
        print("Nem angol betűt adtál meg")
'''
max = 0
gyakori = ""
for k,e in betuk.items():
    if e > max:
        max = e
        gyakori = k
print(max,k)