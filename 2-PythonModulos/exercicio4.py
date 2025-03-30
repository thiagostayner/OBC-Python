'''
* Advinhe o número
-> Escreva um programa em python que gera um número aleatório para que o usuário tente acertar o número. Algumas sugestões para o programa:
1 - Utilizar um laço de repetição para que o programa execute até que o usuário informe um número referente a opção para sair do programa.
2 - Utilizar o módulo random para gerar valores aleatório dentro de um intervalo. Ex. 1 a 10
3 - Lê o número que o usuário digitar via input e comparar se é o mesmo número que o programa sorteou.
'''

import random

continua = True
num_escolhido = random.randint(1,10)
tentativas = 3

while continua:
    escolha = int(input('Escolha um número: '))
    if escolha == num_escolhido:
        print('Você acertou, deseja jogar novamente? Digite 0 para Sair, ou qualquer tecla para continuar')
        sair = int(input('> '))
        if sair == 0:
            print('Obrigado por jogar')
            continua = False
        else:
            num_escolhido = random.randint(1, 10)
            tentativas = 3
            print(f'Novo número foi sorteado, você tem {tentativas} tentativas')
    else:
        tentativas -= 1
        print(f'Você errou, restam {tentativas} tentativas.')
        if tentativas == 0:
            print(f'Acabaram suas chances o número sorteado foi {num_escolhido}, deseja jogar novamente? Digite 0 para Sair ou qualquer tecla para continuar')
            sair = int(input('> '))
            if sair == 0:
                continua = False
            else:
                num_escolhido = random.randint(1, 10)
                tentativas = 3
                print(f'Novo número foi sorteado, você tem {tentativas} tentativas')