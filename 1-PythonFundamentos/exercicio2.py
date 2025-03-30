'''
Exercício 2:
* Substituindo caractere repetido:
-> Escreva um programa Python para obter uma string de uma determinada string em que todas as ocorrências de seu primeiro caractere foram alteradas para '$', exceto o próprio primeiro caractere.
Ex: fifa 23 -> fi$a 23

*troca de caracteres:
-> Escreva um programa Python para obter uma única strings de duas strings fornecidas separadas por um espaço e troque os dois primeiros caracteres de cada string.
Ex: abc svz -> xvc abz
'''
# #Exercicio 1
# nome = str(input('Digite uma palavra: '))
# char = nome[0].lower()
# novoNome = nome.replace(char, '$')
# novoNome = char + novoNome[1:]
# print(novoNome)

# #Exercicio 2
# str1 = str(input('Digite uma palavra: '))
# str2 = str(input('Digite uma segunda palavra: '))
# inicio1 = str1[0:2]
# inicio2 = str2[0:2]

# novaStr = str1.replace(str1[0:2] , inicio2) + ' ' + str2.replace(str2[0:2] , inicio1)
# print(novaStr)

# #solução do professor
# str1 = str(input('Digite uma palavra: '))
# str2 = str(input('Digite uma segunda palavra: '))
# novaStr1 = str2[0:2] + str1[2:]
# novaStr2 = str1[0:2] + str2[2:]
# print(novaStr1 + ' ' + novaStr2)

#exercícios chatgpt

'''
1️⃣  Trocar o primeiro e o último caractere de uma palavra
Peça para o usuário digitar uma palavra e troque o primeiro e o último caractere de posição.

✅ Entrada: python
✅ Saída: nythop
'''
# entrada = str(input('Digite uma palavra: '))
# primeira_letra = entrada[0]
# ultima_letra = entrada[-1]
# nova_entrada = ultima_letra + entrada[1:len(entrada) - 1] + primeira_letra

# print(nova_entrada)

'''
2️⃣ Repetindo os três primeiros caracteres
Receba uma palavra e exiba os três primeiros caracteres dela repetidos duas vezes no final.

✅ Entrada: caderno
✅ Saída: cadernocadcad
'''

# entrada = str(input('Digite uma palavra: '))
# nova_entrada = entrada + entrada[0:3] + entrada [0:3]

# print(nova_entrada)

'''
3️⃣ Criando uma string espelhada
Peça uma palavra e retorne ela junto com sua versão ao contrário.

✅ Entrada: espelho
✅ Saída: espelhoohlepse
'''

# entrada = str(input('Digite uma palavra: '))
# nova_entrada = entrada + entrada[::-1]
# print(nova_entrada)

'''
4️⃣ Removendo o segundo e o penúltimo caractere
O usuário digita uma palavra, e você retorna a versão dela sem o segundo e o penúltimo caractere.

✅ Entrada: computador
✅ Saída: cmputadr
'''

# entrada = str(input('Digite uma palavra: '))
# nova_entrada = entrada[0] + entrada[2:len(entrada) - 2] + entrada[-1]
# print(nova_entrada)

'''
5️⃣ Pegando apenas os caracteres das posições pares
Receba uma palavra e exiba apenas os caracteres que estão nas posições pares (começando do 0).

✅ Entrada: python
✅ Saída: pto
'''

# entrada = str(input('Digite uma palava: '))
# nova_entrada = entrada[0::2]
# print(nova_entrada)

'''
2️⃣ Contar o número de letras "a"
Peça uma palavra ao usuário e conte quantas vezes o caractere "a" aparece nela. Exemplo:

Entrada: banana
Saída: 3
'''

# entrada = str(input('Digite uma palavra: ')).count('a')
# print(entrada)

'''
3️⃣ Concatenar a primeira e a última letra
Dada uma palavra, junte a primeira e a última letra da palavra. Exemplo:

Entrada: programacao
Saída: po
'''

# entrada = str(input('Digite uma palavra: '))
# nova_entrada = entrada[0] + entrada[-1]
# print(nova_entrada)

'''
5️⃣ Retirar a última letra
Receba uma palavra e mostre ela sem a última letra. Exemplo:

Entrada: computador
Saída: computado
'''
entrada = str(input('Digite uma palavra: '))
nova_entrada = entrada[0:-1]
print(nova_entrada)