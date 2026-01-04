a, b = 1, 3
a, b = b, a

pessoa = {
    'nome' : 'Aline',
    'sobrenome' : 'Moreira'
}

dados_pessoa = {
    'idade': 18,
    'altura' : 1.6
}

info_pessoa = {**pessoa, **dados_pessoa, 'bruno': 29}
print(info_pessoa)