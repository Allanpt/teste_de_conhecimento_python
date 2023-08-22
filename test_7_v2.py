import os

print("Bem vindo a lista de compras!")
lista_de_compras = []

while True:
    print("Selecione uma opção:")
    opcao = input("Inserir(i), Apagar(a), Listar(l): ")

    if len(opcao) > 1:
        print()
        print("Digite apenas uma letra! ")
        print()
        continue

    if opcao not in "ial":
        print()
        print("Eu não conheço este comando! Tente: 'i', 'a' ou 'l' ")
        print()
        continue

    if opcao == "i":
        os.system("cls")
        objeto_do_mercado = input("O que você quer inserir na lista: ")
        lista_de_compras.append(objeto_do_mercado)
        print()
        print(f"{objeto_do_mercado} foi ADICIONADO na lista de compras")
        print()

    if opcao == 'l':
        if len(lista_de_compras) == 0:
            print()
            print("A lista está vazia")
            print()

        else:
            os.system("cls")
            print()
            for i, item in enumerate(lista_de_compras):
                print(i, item)
            print()  

    try:
        if opcao == "a":
            os.system("cls")
            print()
            for i, item in enumerate(lista_de_compras):
                print(i, item)
            num_objeto_do_mercado = int(
                input("Insira o número que você quer apagar na lista: ")
            )

            removido = 0
            for i, item in enumerate(lista_de_compras):
                if i  == num_objeto_do_mercado:
                    lista_de_compras.pop(num_objeto_do_mercado)
                    print()
                    print(f"{num_objeto_do_mercado} foi REMOVIDO da lista de compras")
                    print()
                    removido += 1
                    continue
                   
            if removido == 0:
                print()
                print(f"{num_objeto_do_mercado} NÃO ENCONTRADO na lista de compras")
                print()
    except:
        print()
        print("Esse não é um número válido")
        print()

    
