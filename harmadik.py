#3. Írjuk ki az első 19-cel osztható szám indexét!

def három(lista):
    i =0
    index=0
    megvan=False

    while(not megvan and i<len(lista)):

        if lista[i]%19==0:
            index=i
            megvan=True
        i+=1
    print(index)