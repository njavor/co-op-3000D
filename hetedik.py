#7. Mennyi a sorozatban található egyik legkisebb szám indexe?

from csv import list_dialects
from xml.dom.minidom import Element


def hét(lista):
    index=0
    legkisebb = lista[0]
    i=0

    while i<len(lista):
        if lista[i]<legkisebb:  
            legkisebb =lista[i]
            index =i
            i+=1

    print (index)
