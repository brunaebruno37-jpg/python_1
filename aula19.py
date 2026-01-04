x = 1 

def escopo():
    x = 10

    def outra_funcao():
        y = 2
        print(x,y)
    outra_funcao()
    print(x)

escopo()


def soma():
    x = 1 
    y = 2
    def valores():
        resultado = x + y
        print(resultado)
        
    valores()

soma()