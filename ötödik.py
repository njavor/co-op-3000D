#5. Van-e a sorozatban olyan szám, amelyik 1 és 10 közé esik?
def öt(lista):
    i = 0
    while(i < len(lista) and not(0 <= lista[i] <= 10)):
        i+=1
    print("Van a sorozatban 0 és 10 közé eső szám" if i > len(lista) else "Nincs a sorozatban 0 és 10 közé eső szám")