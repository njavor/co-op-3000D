#6. Hány 18-cal osztható szám található a sorozatban?
def hat(lista):
    j = 0
    for i in len(lista):
        if (lista[i] % 18 == 0):
            j+=1
    print(f"{j} 18-al osztható szám van a sorozatban")
