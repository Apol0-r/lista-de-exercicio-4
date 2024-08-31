def uniao(lista1,lista2,listaN = [], f = 0, i = 0):
    if f < len(lista2):
        if lista2[f] not in lista1:
            listaN += [lista2[f]]
        return uniao(lista1,lista2,listaN, f +1)
    
    if i < len(lista1):
        if lista1[i] not in listaN:
            listaN += [lista1[i]]
        
        return uniao(lista1,lista2,listaN,f, i+1)
        


    return listaN



def main():
    l1 = [1,2,3,3,4,1,5,6]
    l2 = [1,5,3]

    listaNova = uniao(l1,l2)

    print(sorted(listaNova))

main()