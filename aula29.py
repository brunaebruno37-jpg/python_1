def imprimir_modelos(nao_impressos, ja_impressos):
    while nao_impressos:
        imprimindo = nao_impressos.pop()
        print(f'imprimindo modelos {imprimindo}')
        ja_impressos.append(imprimindo)

def modelos_ja_imprimidos(modelos_completos):
    print(f'Segue os modelos já imprimidos! ')
    for modelo_completo in modelos_completos:
        print(modelo_completo)

modelos_nao_impressos = ['Iphone', 'Samsung', 'Xiaomi']
modelo_ja_impressos = []


imprimir_modelos(modelos_nao_impressos[:], modelo_ja_impressos)
print()

modelos_ja_imprimidos(modelo_ja_impressos)