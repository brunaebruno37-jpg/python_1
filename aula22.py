pessoa = {
    'nome' : 'Luiz Ótavio',
    'sobrenome' : 'Miranda',
    'idade' : 18,
    'altura' : 1.8,
    'endereço' : [
        {'rua' : 'joão' , 'numero' : 1234},
        {'rua' : 'maciel' , 'numero' : 1234}
    ]
}

for chave in pessoa:
    print(chave,pessoa[chave])