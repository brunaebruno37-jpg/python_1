lista = []

while True:
    print('selecione uma opção')
    usuario = input('[i]nserir [a]pagar [l]istar:' )
    if usuario == 'i':
        novo_item = input('O que vai inserir na lista: ')
        lista.append(novo_item)
        print(lista)
    
    elif usuario == 'l':
        if usuario == 0:
            print('A sua lista está vazia.')
        lista_enumerada = enumerate(lista)
        for item in lista_enumerada:
            print(item)

    else:
        print('por favor digite ou i ou a ou l')

    