nome = input("Digite seu nome: ")

tamanho_do_nome = len(nome)

contador = 0

while contador < tamanho_do_nome:
    print(f'*{nome[contador]}',end='' )
    contador += 1