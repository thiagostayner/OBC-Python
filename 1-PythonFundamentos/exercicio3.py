'''
Exercício 3:
* Cálculo da Distância:
-> Escreva um programa que pergunta a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km, e R$ 0,35 para viagens mais longas.

* Aumento salário funcionário:
-> Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
Para Salários superiores a R$ 1.250,00, calcule um aumento de 10%.
para os Inferiores ou iguais, de 15%.
'''

# Exercício 1
distancia = float(input('Informe a distância que irá percorrer: '))

if distancia <= 200:
    valor = distancia * 0.5
else:
    valor = distancia * 0.35
print(f'O valor cobrado será de R$ {valor:.2f}')

# Exercício 2
salario = float(input('Informe o seu salário: '))

if salario > 1250:
    aumento = (salario * 0.1)
else:
    aumento = (salario * 0.15)
print(f'Você receberá um aumento e seu novo salário será de R$ {aumento:.2f}')