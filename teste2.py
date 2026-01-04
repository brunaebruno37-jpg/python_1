lista_de_sanduiches = ['baurú','moda da casa','misto','simples']

sanduiche_finalizados = []

pedido = True

while pedido:
    print('Faça um pedido do seu sanduiche')
    for item in lista_de_sanduiches:
        print(item)
    cliente = input('Qual o sanduiche que você deseja: ')

    print()

    sanduiche_finalizados.append(cliente)
    if cliente == 'baurú':
        print('Não é possível produzir esse sanduíche, estamos sem o matérial para ele.')
        sanduiche_finalizados.remove('baurú')
    print(f'Sanduiches pedidos {sanduiche_finalizados}')
    print()

    continuar_pedido = input('Deseja continuar com o seu pedido: (Sim/não)')
    
    if continuar_pedido == 'não':
        pedido = False
        print()
