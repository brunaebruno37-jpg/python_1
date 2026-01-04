nome = input('Por favor digite seu nome: ')
idade = input('Por favor digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[-1:-6:-1]}')
    if ' ' in nome:
        print(f'Seu nome contem espaços')
    else:
        print('seu nome não contém espaços')
    
    print(f'Seu nome contém {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A Ultima letra do seu nome é {nome[4]}')

elif nome or idade:
    print('Desculpe, você deixou campos vazios')

    