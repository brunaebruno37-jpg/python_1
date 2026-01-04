entrada = input('[E]ntrar [S]sair: ')
print(entrada)
senha_digitada = input('senha: ')

senha_permitida = '123456'

if (entrada =='E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrada com sucesso')

else:
    print('Saiu')

