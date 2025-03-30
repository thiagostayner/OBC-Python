num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

# Aritméticos
soma = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
resto = num1 % num2
exp = num1 ** num2
print(f'Resto da divisão de {num1} por {num2} é {resto}')
print(f'Potência do número {num1} por {num2} é {exp}')

# Comparação
maior = num1 > num2
menor = num1 < num2
igual = num1 == num2
diferente = num1 != num2
maiorIgual = num1 >= num2
menorIgual = num1 <= num2

print(f'Os números {num1} e {num2} são iguais? {igual}')
print(f'O número {num1} é maior ou igual ao {num2}? {maiorIgual}')

# Atribuição
num1 += 1 #num1 = num1 + 1
num1 -= 1 #num1 = num1 - 1
num1 *= 1 #num1 = num1 * 1
num1 /= 1 #num1 = num1 / 1