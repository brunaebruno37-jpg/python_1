numero = 0

while numero < 50:
    numero += 1
    

    if numero == 10:
        continue

    if numero > 11 and numero < 20:
        print('manhosa, bebe')
        continue

    if numero == 30:
        break

    print(numero)


print(numero) 