import random

Cpf = ''
for i in range(9):
    Cpf += str(random.randint(0,9))

Cpf_numero_repetido = Cpf[0] * len(Cpf)

if Cpf == Cpf_numero_repetido:
    print("CPF inválido! Não é aceito CPF com numeros idênticos")


# primeiro dígito
soma = 0
multiplicador = 10
for i in range(9):
    soma += int(Cpf[i]) * multiplicador
    multiplicador -= 1

resultado = (soma * 10) % 11

penultimo_numero_CPF = resultado if resultado <= 9 else 0

Cpf = Cpf + str(penultimo_numero_CPF)

# segundo dígito
soma_2 = 0
multiplicador_2 = 11
for i in range(10):
    soma_2 += int(Cpf[i]) * multiplicador_2
    multiplicador_2 -= 1

resultado_2 = (soma_2 * 10) % 11

ultimo_numero_CPF = resultado_2 if resultado_2 <= 9 else 0

Cpf = Cpf + str(ultimo_numero_CPF)

print()

print(Cpf)
