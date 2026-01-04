hora = input('diga que horas são: ')


try:
    hora = float(hora)
    if hora >= 0 and hora <=12:
        print('Bom dia')

    elif hora >= 12 and hora <=18:
        print('Boa tarde!')

    elif hora >= 18 and hora <= 23:
        print('Boa noite!')


    else:
        print('diga que horas são!')
except:
    print('Você não disse que horas são!')