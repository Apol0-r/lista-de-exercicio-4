def inteiroReal(lista, i = 0): #a
    if i < len(lista):
        if isinstance(lista[i], int) or isinstance(lista[i], float):
            return inteiroReal(lista, i+ 1)
        else:
            return False
    
    return True


def mediaLista(lista): #b
    return sum(lista)/len(lista)

def maiorMenor(lista, i = 0, max = 0, min = 0): #c

    if i == 0:
        max = lista[i]
        min = lista[i]
        return maiorMenor(lista, i+1, max, min)
    if i < len(lista):

        if lista[i] < min:
            min = lista[i]

        elif lista[i] > max:
            max = lista[i]

        return maiorMenor(lista, i+1, max, min)

    return max, min 
    
def reverse(lista, listaR = [], i  = 1,): #d
    if i <= len(lista):
        listaR += [lista[-i]]

        return reverse(lista, listaR, i + 1)
    
    return listaR

def vezesN(lista,x, i = 0,contador = 0): #e
    if i < len(lista):
        if x == lista[i]:
            contador += 1
        
        return vezesN(lista,x, i+1,contador)
    
    return contador

def divisores(n, i = 1,divisor = []): #f
    if i <= n:
        if n%i == 0:
            divisor += [i]
        return divisores(n, i+1, divisor)

    return divisor


    

def main():
    lista = [1,2,3,0,10,2,2,4]
    ir = inteiroReal(lista)
    media = mediaLista(lista)
    maior,menor = maiorMenor(lista)
    reverso = reverse(lista)
    vezes = vezesN(lista,2)
    divid = divisores(24)

    print(
        lista,
        ir,
        media,
        f"MAIOR: {maior}, MENOR : {menor}",
        reverso,
        vezes,
        divid,
        sep = "\n"
        )


main()