palavra_secreta = 'jesus'
letra_acertada = ''
numero_tentativas = 0


while True:
    letra_digitada = input('digite uma letra: ')
    numero_tentativas += 1
    if len(letra_digitada) > 1:
        print('digite apenas uma letra. ')
        continue

    if letra_digitada in palavra_secreta:
        letra_acertada += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('palavra formada: ',palavra_formada)

    if palavra_formada == palavra_secreta:
        print('VOCÊ GANHOU!! PARABÉNS!!!')
        print('A palavra secreta era: ', palavra_secreta)
        print('Seu numero de tentativas foram: ',numero_tentativas)