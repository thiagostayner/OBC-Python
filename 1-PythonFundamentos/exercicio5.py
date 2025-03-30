'''
Exercício5:
* Conta letras maiúsculas e minúsculas:
-> Escreva uma função Python que receba um string e conte o número de letras
maiúsculas e minúsculas desta string.

* Lista números pares e ímpares de uma lista:
-> Escreva uma função Python para imprimir os números pares e ímpares em duas listas separadas para cada uma
'''

# Exercício 1
def contador (palavra):
    minusculas = 'abcdefghijklmnopqrstuvwxyz'
    contMin = 0
    contMai = 0
    for i in palavra:
        if i in minusculas:
            contMin += 1
        else:
            contMai += 1
    print(f'Existe {contMin} minúsculas e {contMai} maiúsculas')

palavra = str(input('Digite uma palavra: (obs: não colocar espaços ou caracteres especiais)'))
contador(palavra)

#solução do professor

def verificador (texto):
    tipo = {'Maiúsculas' : 0, 'Minúsculas' : 0}
    for char in texto:
        if char.isupper():
            tipo['Maiúsculas'] += 1
        elif char.islower():
            tipo['Minúsculas'] += 1
    print(f'Texto Original {texto}')
    print(f'Quantidade de maiúsculas {tipo["Maiúsculas"]}')
    print(f'Quantidade de minúsculas {tipo["Minúsculas"]}')

verificador('A Melhor Forma De Prever o Futuro é Criá-lo')


# Exercício 2
def parOuImpar (qtdeNums):
    par = []
    impar = []
    for i in range(qtdeNums):
        num = int(input(f'Digite o {i + 1}º número: '))
        if num % 2 == 0:
            par.append(num)
        else:
            impar.append(num)
    print(f'Os números pares são {par} e os impares são {impar}')

qtdeNums = int(input('Informe quantos números deseja preencher: '))
parOuImpar(qtdeNums)


