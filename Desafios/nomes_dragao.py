'''
O Enigma dos Nomes do Dragão 🐉
Você é um aventureiro destemido que busca a sabedoria antiga dos Dragões. Sua missão é decifrar o enigma dos nomes dracônicos para obter acesso ao conselho secreto dos Dragões! Para isso, você precisará criar uma função em Python que reorganize as letras de um título dracônico secreto.

Os Dragões são criaturas místicas e sábias, e seus nomes seguem uma regra especial: qualquer nome dracônico pode ser transformado em um palíndromo usando algumas manipulações mágicas. Um palíndromo é uma sequência que pode ser lida da mesma forma da esquerda para a direita e vice-versa.

Regras 🔍
Você deve criar uma função chamada gerar_nome_dragonico.
Ela deve receber uma string como entrada representando o nome dracônico secreto.
A função deve retornar a menor versão de um palíndromo que pode ser feita a partir das letras do nome dado.
Caso não seja possível formar um palíndromo, a função deve retornar a string 'Impossível formar um palíndromo'.
Exemplo de Entrada e Saída ⚔️
Entrada: 'eragon'
Saída: 'Impossível formar um palíndromo'

Entrada: 'malayalam'
Saída: 'malayalam'
'''

def gerar_nome_dragonico(string):
    manipulacao = string[::-1]
    if manipulacao == string:
        resultado = manipulacao
    else:
        resultado = 'Impossível formar um palíndromo'
    return resultado

print(gerar_nome_dragonico('eragon'))
print(gerar_nome_dragonico('malayalam'))
