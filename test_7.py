lista_de_compras = ['arroz', 'feijão', 'sal', 'abacate', 'banana']

while True:
    for alimento in lista_de_compras:
        print(alimento)


    operacao = input("Inserir alimentos?(i) Deletar alimentos?(d) ")

    if operacao == 'i':

        inserir_alimento = input("Qual alimento você quer adicionar? ")
        lista_de_compras.append(inserir_alimento)


    if operacao == 'd':

        inserir_alimento = input("Qual alimento você quer deletar? ")
        for indice_alimentos, *_ in enumerate(lista_de_compras):
            if lista_de_compras[indice_alimentos] == inserir_alimento:
                del lista_de_compras[indice_alimentos]
                print("Alimento deletado")
            
            
    opcao = input("Saír? (s/n)")

    if opcao == 'n':
        continue
    else:
        print("Saindo.... Até mais!")
        break