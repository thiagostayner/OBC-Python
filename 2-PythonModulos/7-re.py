import re

text = '''OneBitCode: Transformamos pessoas em programadores sem limites'''
# 1 - indice inicial e final de palavras
# O r significa que estamos trabalhando com uma string bruta

match = re.search(r'pessoas em programadores', text)
print(f'Índice inicial {match.start()}')
print(f'Índice final {match.end()}')

# 2 - Buscando o índice que possui o ponto
site = 'https://onebitcode.com'
# match = re.search(r'.', site)
match = re.search(r'\.', site)
print(match)

# 3 - Buscando uma lista de caracteres dentro de uma frase
padrao = "[a-m]"
result = re.findall(padrao, text)
print(text)
print(result)

# 4 - Veificando o início de uma string
regra = r'^A'
frases = ['A casa está suja', 'O dia está lindo', 'Vamos passear']
for f in frases:
    if re.match(regra, f):
        print(f'Corresponde: {f}')
    else:
        print(f'Não corresponde: {f}')

# 5 - Verificando o final da string
regra_final = r'!$'
frases2 = 'O dia está lindo!'
match = re.search(regra_final, frases2)
if match:
    print('Sim corresponde')
else:
    print('Não corresponde')