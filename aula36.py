def zipper(lista1, lista2):
    intervalo_maximo = min(len(lista1), len(lista2))
    return [
        (lista1[i], lista2[i]) for i in range(intervalo_maximo)
    ]

lista1 = ['salvador', 'ubatuba', ' belo horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

print(zipper(lista1,lista2))  