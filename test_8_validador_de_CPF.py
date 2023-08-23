"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

while True:
    Cpf = input("Digite um CPF: ")

    if len(Cpf) != 14:
        print("CPF inválido! Tente neste formato: 999.999.999-99")
        continue

    Cpf_sem_pontos = Cpf.split(".")
    Cpf = ''.join(Cpf_sem_pontos)
    Cpf_sem_traços = Cpf.split("-")
    Cpf = ''.join(Cpf_sem_traços)
    
    if len(Cpf) != 11:
        print("CPF inválido! A quantidade de números não é válida.")
        continue

    Cpf_numero_repetido = Cpf[0] * len(Cpf)

    if Cpf == Cpf_numero_repetido:
        print("CPF inválido! Não é aceito CPF com numeros idênticos")
        continue
    
    try:
        Cpf_int = int(Cpf)
    except:
        print("CPF inválido! Digite apenas números inteiros.")

    # primeiro dígito
    soma = 0
    multiplicador = 10
    for i in range(9):
        soma += int(Cpf[i]) * multiplicador
        multiplicador -= 1

    resultado = (soma * 10) % 11

    valor_final = resultado if resultado <= 9 else 0

    # segundo dígito
    soma_2 = 0
    multiplicador_2 = 11
    for i in range(10):
        soma_2 += int(Cpf[i]) * multiplicador_2
        multiplicador_2 -= 1

    resultado_2 = (soma_2 * 10) % 11

    valor_final_2 = resultado_2 if resultado_2 <= 9 else 0

    print("CPF VÁLIDO") if valor_final == int(Cpf[9]) and valor_final_2 == int(Cpf[10]) else print("CPF inválido!")
    print()
    print(f"O primeiro dígito do CPF tem que ser {valor_final} e o segundo {valor_final_2}")
