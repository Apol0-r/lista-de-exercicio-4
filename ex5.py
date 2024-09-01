def intersecao(lista1,lista2, listaN = [], i = 0):
    if i < len(lista1):
        if lista1[i] in lista2 and lista1[i] not in listaN:
            listaN += [lista1[i]]
        return intersecao(lista1,lista2,listaN, i+1)
        
    return listaN

def main():
    l1 = [1,2,3,3,4,8]
    l2 = [1,5,3,4]

    listaN = intersecao(l1,l2)

    listaN2 = intersecaoSet(l1,l2)

    print(listaN,listaN2)



def intersecaoSet(lista1,lista2, listaN = []):
    """
    coleção não ordenada de elementos únicos
    """
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    listaN = conjunto1 & conjunto2

    return list(listaN)

main()