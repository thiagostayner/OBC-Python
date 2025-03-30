'''
Exercicio 1:
* Antecessor e Sucessor de um número:
-> Escreva um programa em Python que leia um número e represente o número antecessor e sucessor desse número que foi lido, utilizando operadores de atribuição.

* Média de 4 notas:
-> Escreva um programa em Python que leia quatro números e calcule a média entre esses números
'''

#Desafio 1
numero = int(input('Digite um número: '))
sucessor = numero + 1
antecessor = numero - 1

print(f'O número escolhido foi {numero} e seu sucessor é {sucessor} e o antecessor {antecessor}')

#Desafio2
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))
nota4 = float(input('Informe a quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'A media das notas {nota1, nota2, nota3, nota4} é {media}.')