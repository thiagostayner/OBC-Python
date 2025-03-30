'''
Exercício 4:
* Contagem Regressiva:
-> Faça um programa para escrever a contagem regressiva do lançamento de um foguete.
O programa deve imprimir 10,9,8,...,1,0 e disparar um "beep".

* Tabuada:
-> Faça um programa que calcule a tabuada de um número, com valores iniciais e finais informados pelo usuário.
'''

# Exercício 1
import winsound
import time
cont = 10

while cont > -1:
    print(cont)
    cont -= 1
    time.sleep(1)

winsound.Beep(1500, 500)

# Exercício 2
num = int(input('Informe o número para saber sua tabuada; '))
numInicial = int(input('Informe o valor inicial que deseja: '))
numFinal = int(input('Informe o valor final que deseja: '))

for i in range(numInicial, numFinal + 1):
    resultado = i * num
    print(f'{i} x {num} = {resultado}')