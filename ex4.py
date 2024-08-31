def listaVirgem(lista, listaN = [], i = 0):
    if i < len(lista):
        if lista[i] not in listaN:
            listaN += [lista[i]]
        return listaVirgem(lista,listaN, i +1)
    
    return listaN

def main():

    l1 = [1,2,2,2,5,3,5]

    listanova = listaVirgem(l1)

    print(sorted(listanova))

main()