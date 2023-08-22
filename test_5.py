while True:
    n1 = input("Digite um numero: ")
    n2 = input("Digite outro numero: ")
    operacao = input(
        "Qual operação você quer fazer? (soma '+', subtração '-', multiplicação '*', ou divisão '/') "
    )

    try:

        if operacao == "+":
            resultado = n1 + n2
        elif operacao == "-":
            resultado = n1 - n2
        elif operacao == "*":
            resultado = n1 * n2
        elif operacao == "/":
            resultado = n1 / n2

        print(resultado)
        print()
        pergunta = input("Continuar operação (s/n)? ").lower().startswith("n")

        if pergunta is True:
            break
    
    except:
        print("Isso não é um número válido! ")
