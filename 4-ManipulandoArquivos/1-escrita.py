nome = input('Digite o seu nome: ')
'''
- Arquivos:
1- opção w - escrever
2 - opção a - append
3 - opção r - read
'''

# Alternativa 1
# file = open('nomes.txt', 'a')
# file.write(f'{nome}\n')
# file.close()

# Alternativa 2
with open('4-ManipulandoArquivos/nomes.txt', 'a') as file:
    file.write(f'{nome}\n')