lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = [1, 2, 3, 4]

lista3 = [x + y for x, y  in zip(lista1, lista2)]
print(lista3)



'''for i in range(len(lista2)):
    lista3.append(lista1[i] + lista2[i])
print(lista3)'''


