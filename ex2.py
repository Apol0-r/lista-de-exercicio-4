def main():
    lista = [2,2,2,7,5,8]
    lista_primos = listaPrimo(lista)

    
    print(lista,lista_primos,sep="\n")

def ehPrimo(n, i = 1,contador = 0):
    if i <= n:
        if n%i == 0:
            contador += 1 

        return ehPrimo(n, i+1, contador)
    
    if contador == 2:
        return True
    
def listaPrimo(lista, listaN = [],i = 0):
    if i < len(lista):
        if ehPrimo(lista[i]):
            listaN += [lista[i]]
        
        return listaPrimo(lista,listaN, i + 1)
    
    return listaN

main()