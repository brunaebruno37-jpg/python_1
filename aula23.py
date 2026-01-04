pessoa = [
    {
        'pergunta' : 'Quanto é 2+2?',
        'Opções' : ['1','3','4','5'],
        'resposta' : '4',
},
{
        'pergunta' : 'Quanto é 2+2?',
        'Opções' : ['1','3','4','5'],
        'resposta' : '4',
},
{
        'pergunta' : 'Quanto é 2+2?',
        'Opções' : ['1','3','4','5'],
        'resposta' : '4',
},
]


qtd_acertos = 0
for pergunta in pessoa:
    print(f'pergunta:',pergunta['pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i})',opcao)
        print()

        acertou = False
        escolha = input('Escolha uma opção: ')
        qtd_opcoes = len(opcoes)

        escolha_int = None
        if escolha.isdigit():
            escolha_int = int(escolha)

        if escolha_int is not None:
            if escolha_int >= 0 and escolha_int < qtd_opcoes:
                if opcoes[escolha_int] == pergunta['resposta']:
                    acertou = True

        if acertou:
            qtd_acertos += 1
            print('ACERTOU!!')

        else:
            print('ERROU!')


    print('Você acertou', qtd_acertos)
    print('De', len(pergunta), ' perguntas')