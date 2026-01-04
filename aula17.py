cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo = 10

resultado = 0
for digito in nove_digitos:
    resultado += int(digito) * contador_regressivo
    contador_regressivo -= 1
digito_1 = resultado * 10 % 11  
digito_1 = digito_1 if digito_1 <= 9 else 0 

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_2  = 0
for digito in dez_digitos:
    print(int(digito) * contador_regressivo_2)
    contador_regressivo_2 -= 1
digito_2 = resultado_2 * 10 % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print(digito_2)
