def criar_multplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


x2 = criar_multplicador(3)
x3 = criar_multplicador(4)
x4 = criar_multplicador(4)

print(x2(2))
print(x3(2))
print(x4(5))