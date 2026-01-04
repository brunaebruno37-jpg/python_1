lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 2, 4, 6, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 3, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 7, 6, 7, 8, 9, 10]
]

def encontreoprimeiroduplicado(lista_de_inteiros):
    numero_chegados = set()
    primeiro_duplicado = -1

    for numero in lista_de_inteiros:
        if numero in numero_chegados:
            numero_chegados = numero
            break


        numero_chegados.add(numero)
         
    return primeiro_duplicado

for lista in lista_de_listas_de_inteiros:
    print(
        lista,
        encontreoprimeiroduplicado(lista)
        
        )