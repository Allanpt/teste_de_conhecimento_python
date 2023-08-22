"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.

Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra. Qual o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.

Se a letra digitada estiver na palavra-secreta; exiba a letra; 

Se a letra digitada não estiver na palavra secreta; exiba *

Faça a contagem de tentativas do seu usuário.

"""
import os

palavra = 'allan'
letras_anteriores = ""
tentativa = 0

while True:

    
    tentativa += 1

        

    print(f'Tentativa {tentativa}')

    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print()
        print("Digite apenas uma letra! ")
        print()

        continue


    if letra in palavra:
        letras_anteriores += letra
    
    palavra_completa = ''
    for palavra_secreta in palavra:
        
        if palavra_secreta in letras_anteriores:
            print(palavra_secreta, end="")

            
            palavra_completa += palavra_secreta
        else:
            print('*', end="")
    print()
    print()
    
    if palavra_completa == palavra:
        os.system('cls')
        print("Parabéns! Você ganhou o jogo!")
        print('FIM')
        break
    