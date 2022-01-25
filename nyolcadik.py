# 8. Írjuk ki a sorozatban található 17-tel vagy 18-cal osztható számok négyzetét!

def nyolc(lista):
    számolás=0
    
    for elem in lista:
        if lista[i]%17==0 or lista[i]%18==0:
            számolás+=elem


    számolás*=számolás

    print (számolás)
