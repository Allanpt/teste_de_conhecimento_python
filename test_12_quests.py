perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
acertos = 0
for questões in perguntas:
    chave_pergunta = list(questões.keys())[0]
    valor_pergunta = questões.get('Pergunta')

    print(f"{chave_pergunta}: {valor_pergunta}")
    print()

    chave_opcoes = list(questões.keys())[1]
    print(f'{chave_opcoes}:')

    valor_opcoes = questões.get('Opções')

    num_de_alternativas = 0
    valor_resposta = questões.get('Resposta')

    for opcoes in valor_opcoes:
        print(f'{num_de_alternativas}) {opcoes}')
        if opcoes == valor_resposta:
            alternativa_correta = num_de_alternativas
        num_de_alternativas += 1
    opcao_escolhida = input("Escolha uma opcao: ")   

    
    if int(opcao_escolhida) == alternativa_correta:
        acertos += 1
        print("ACERTOU!!")
    else:
        print("ERROU!!!!")

    print()
print(f'Você teve {acertos} acertos!')
    
    