def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_negociar):
        nonlocal valor_final
        valor_final += valor_a_negociar
        return valor_final
    return interna

c = concatenar('Olá')

print(c(', tudo bem?')) 