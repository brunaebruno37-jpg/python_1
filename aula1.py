cpf = '74682489070'
nove_digitos = cpf[:9] 
contador_regressivo = 10

multiplicacao = 0
for digito in nove_digitos:
    multiplicacao += int(digito) * contador_regressivo
    contador_regressivo -= 1
digito = (multiplicacao * 10) % 11
digito = digito if digito <= 9 else 0
print(digito)



#cpf = '74682489070'
nove_digitos = cpf[:9] + '7'
contador_regressivo = 11

multiplcacao = 0
for digito in nove_digitos:
    multiplcacao += int(digito) * contador_regressivo
    contador_regressivo -= 1
digito2 = (multiplcacao * 10) % 11
if digito2 <= 9:
    digito2 = 0
    print(digito2)
else:
    print(digito2)