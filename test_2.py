numero_inteiro_str = input("Digite um numero inteiro: ")

print()
if numero_inteiro_str.isdigit():
    numero_inteiro = int(numero_inteiro_str)
    eh_par_impar = numero_inteiro % 2
    print()
    if eh_par_impar == 0:
        print(f"O número {numero_inteiro} é par")
    else:
        print(f"O número {numero_inteiro} é ímpar")
else:
    print("Você não digitou um número inteiro!")
