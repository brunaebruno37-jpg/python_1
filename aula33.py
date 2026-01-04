def concatenar(string_inicial):
    valor_final = string_inicial 
    
    def interna(valor_a_concatelar):
        nonlocal valor_final
        valor_final += valor_a_concatelar
        return valor_final
    return interna

c = concatenar('a')

print(c('b'))
print(c('c'))
print(c('d'))