num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
operacao = int(input('Digite 1 para Somar, 2 para Subtrair, 3 para Multiplicar e 4 para Dividir: '))

if operacao == 1:
    resultado = num1 + num2
    print(f'A soma entre {num1} + {num2} = {resultado}')
elif operacao == 2:
    resultado = num1 - num2
    print(f'A subtração entre {num1} - {num2} = {resultado}')
elif operacao == 3:
    resultado = num1 * num2
    print(f'O resultado da multiplicação entre {num1} * {num2} = {resultado}')
elif operacao == 4:
    resultado = num1 / num2
    print(f'O resultado da divisão entre {num1} / {num2} = {resultado}')
else:
    print('Opção inválida, selecione 1, 2, 3 ou 4 conforme orientação')

