#4. Igaz-e, hogy minden szám negatív?
def négy(lista):
    i = 0
    while(i < len(lista) and not(lista[i]<0)):
        i+=1
    print("minden szám negatív" if i > len(lista) else "nem minden szám negatív")