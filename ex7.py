def perguntas(lista=[0]*10, contador = 0):
    n = int(input("Digite os valores (um número <0 ou >9 indica o fim da leitura): "))

    if 0 <= n <= 9:
        contador += 1
        lista[n] += 1
        return perguntas(lista,contador)
    
    return lista, contador

def impressora(lista, i = 0):
    if i < len(lista):
        print(f"[{i:02d}] - {"*"*lista[i]}")

        return impressora(lista, i + 1)
    
 
def main():
    lista, contador = perguntas()
    print(f"Números digitados = [{contador}]")
    impressora(lista)

main()