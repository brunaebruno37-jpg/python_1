
from itertools import combinations, permutations, product



def print_list(*args):
    print(*list(*args), sep='\n')
    print()
pessoas = ['joão', 'joana', 'Luiz', ' leticia',]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['Masculino', 'Feminino', 'unisex'],
    ['algodão', 'poliester']
]

#print_list(permutations(pessoas, 2))
#print_list(combinations(pessoas, 2))
print_list(product(*camisetas))



