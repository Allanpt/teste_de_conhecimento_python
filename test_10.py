# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multi(*args):
    multiplier = 1
    for nums in args:
        multiplier *= nums
    return multiplier

print(multi(2,6,5,6,5,7,1))

# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_ou_impar(n):
    num = n % 2

    if num == 0:
        return f"{n} é par" 
    return f"{n} é impar"

print(par_ou_impar(8))