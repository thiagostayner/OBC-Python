'''
* Verificar conteúdo da String
-> Escreva um programa em Python para verificar se uma string contém apenas um determinado conjunto de caracteres (neste caso, a-z, A-Z e 0-9)
'''

import re

def check_caracter(string):
    regra = re.compile(r'[^a-zA-Z0-9]')
    string = regra.search(string)
    return not bool(string)

print(check_caracter('ahsudfhausdfah@sdfu'))
print(check_caracter('!@#$!@#$@#$!'))

