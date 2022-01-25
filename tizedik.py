def tíz(lista):
    vanE = False
    i = 1
    while(i < len(lista)-1 and not vanE):
        if lista[i] < 0 and (lista[i+1] and lista[i-1]) > 0:
            vanE = True
    print(vanE)