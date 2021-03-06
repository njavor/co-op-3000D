"""
Olvassuk be az alábbi fájl tartalmmát egy listába/tömbbe,
majd a következő feladatokat oldjuk meg.
Minden feladat előtt a program írja ki a feladat sorszámát!
1. Mennyi a sorozatban található számok szorzata?
2. Írjuk ki az utolsó 5-tel vagy 7-tel osztható szám indexét!
3. Írjuk ki az első 3-mal és 7-tel osztható szám indexét!
4. Igaz-e, hogy minden szám negatív?
5. Van-e a sorozatban olyan szám, amelyik 1 és 10 közé esik?
6. Hány 18-cal osztható szám található a sorozatban?
7. Mennyi a sorozatban található egyik legkisebb szám indexe?
8. Írjuk ki a sorozatban található 17-tel vagy 18-cal osztható számok négyzetét!
9. Hány eleme van a sorozatnak?
10. Van-e a sorozatban olyan negatív szám, amelynek az összes szomszédja pozitív?
"""

from első import egy
from második import kettő
from harmadik import három
from negyedik import négy
from ötödik import öt
from hatodik import hat
from hetedik import hét
from nyolcadik import nyolc
from kilencedik import kilenc
from tizedik import tíz

lista = []
with open("input.txt","r",encoding="utf8") as f:
    for sor in f:
        lista.append(int(sor))

print("1. Mennyi a sorozatban található számok szorzata?")
egy(lista)
print("2. Írjuk ki az utolsó 5-tel vagy 7-tel osztható szám indexét!")
kettő(lista)
print("3. Írjuk ki az első 3-mal és 7-tel osztható szám indexét!")
három(lista)
print("4. Igaz-e, hogy minden szám negatív?")
négy(lista)
print("5. Van-e a sorozatban olyan szám, amelyik 1 és 10 közé esik?")
öt(lista)
print("6. Hány 18-cal osztható szám található a sorozatban?")
hat(lista)
print("7. Mennyi a sorozatban található egyik legkisebb szám indexe?")
hét(lista)
print("8. Írjuk ki a sorozatban található 17-tel vagy 18-cal osztható számok négyzetét!")
nyolc(lista)
print("9. Hány eleme van a sorozatnak?")
kilenc(lista)
print("10. Van-e a sorozatban olyan negatív szám, amelynek az összes szomszédja pozitív?")
tíz(lista)