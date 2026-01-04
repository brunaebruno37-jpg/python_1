

def executa(funcoes, *args):
    return funcoes(*args)



def soma(x,y):
    return x + y

print(
    executa(
        lambda x, y : x + y, 3, 7
        
    )

)