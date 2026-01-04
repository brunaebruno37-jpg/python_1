lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome' : 'Bruno'}
]

for item in lista:
    if isinstance(item, dict):
        item.update(Amor= 'Deus')
        print(item)