# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.


def multi(n):
    def For(x):
        return n * x
    return For


operacao = multi(5)

print(operacao(2))