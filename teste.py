magicos = ['Bruno', 'Bruna', 'Dora', 'José']

def show_de_magica(magicos):
    for magico in magicos:
        print(magico)

def make_great(funcao):
    for magico in funcao:
        print(f'O grande magico é {magico}')

show_de_magica(magicos)

make_great(magicos[:])

show_de_magica(magicos)
