def ordenada(lista,listaN = [],  i = 0):
    listaN = sorted(lista)
    if lista == listaN:
        return True
    return False
    
    
def  main():

    l1 = [1,5,6,8,9,5]
    l2 = [1,2,3,4,5]
    print(ordenada(l1))
    print(ordenada(l2))

main()