#crie uma função que multiplique todos os argumentos não nomeados recebidos
#retorna o total para uma variavel e mostra o valor

def multiplicar(*args):
    total = 1
    for numero in args:
        total = total * numero
    return total

calculo = multiplicar(1, 2, 3, 4, 5, 6)
print(calculo)
