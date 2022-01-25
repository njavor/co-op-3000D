def kettő(lista):
    i = len(lista)-1
    while 0<=i and not (lista[i] %5 == 0 or lista[i] %7 == 0):
        i-=1
    print(lista[i] if 0<=i else "Nincs 5-tel, vagy 7-tel osztható szám")