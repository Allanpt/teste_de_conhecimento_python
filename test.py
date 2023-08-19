nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
 
#nome contém espaços?

if " " in nome:
    contém_espacos_ou_nao= "Seu nome contém espaços!"
else:
    contém_espacos_ou_nao= "Seu nome NÃO contém espaços!"


while len(nome) == 0 or len(idade) == 0:
    print("Desculpe, você deixou campos vazios. Tente novamente:")
    print()
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
print()
print(f"Seu nome é {nome}")
print(f"Seu nome invertido é {nome[::-1]}")
print(contém_espacos_ou_nao)
print(f"Seu nome contém {len(nome)} caracteres")
print(f"A primeira letra do seu nome é {nome[0]}")
print(f"A última letra do seu nome é {nome[len(nome)-1]}")

