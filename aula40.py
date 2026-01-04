from itertools import groupby

alunos = [
    {'nome' : 'Luiz', 'nota' : 'A'},
    {'nome' : 'Bruno', 'nota' : 'B'},
    {'nome' : 'Roberto', 'nota' : 'C'},
    {'nome' : 'Samuel', 'nota' : 'D'},
    {'nome' : 'Alessandra', 'nota' : 'A'},
    {'nome' : 'Ligia', 'nota' : 'B'},
    {'nome' : 'Bruna', 'nota' : 'C'},
    {'nome' : 'Francisco', 'nota' : 'D'}
]

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)

grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)