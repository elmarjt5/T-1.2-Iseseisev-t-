

#Parandatud math mooduli import
import math
print("Ruudu karakteristikud")

#Float() lisatud et sisend oleks arv
a=float(input('Sisesta ruudu külje pikkus => '))
S=a**2

print("Ruudu pindala", S)
P=4*a
#Parandatud ruutjuure funktsioon sqrt()
print("Ruudu ümbermõõt", P)
di = a*math.sqrt(2)
print("Ruudu diagonaal", round(di,2))

print()
#Üleliigne sulg eemaldatud
print("Ristküliku karakteristikud")

# Lisatud float(), et teisendada tekst arvuks
b=float(input("Sisesta ristküliku 1. külje pikkus => "))
c=float(input("Sisesta ristküliku 2. külje pikkus => "))
S=b*c
#Lisatud puuduvad jutumärgid
print('Ristküliku pindala', S)

# Lisatud puuduv korrutusmärk
P=2*(b+c)
print("Ristküliku ümbermõõt", P)


di = math.sqrt(b**2+c**2)
# Lisatud ümardamine kahe komakohani

print("Ristküliku diagonaal", round(di, 2))
print()
print("Ringi karakteristikud")
# Eemaldatud üleliigne sulg

r = float(input("Sisesta ringi raadiuse pikkus => "))
# Lisatud korrutusmärk

d = 2*r
# Lisatud puuduv koma

print("Ringi läbimõõt", d)
# Parandatud piid

S = math.pi*r**2
print("Ringi pindala", round(S, 2))
C = 2*math.pi*r
# Lisatud ümardamine kahe komakohani
print("Ringjoone pikkus", round(C, 2))




