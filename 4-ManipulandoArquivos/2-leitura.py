'''
- Arquivos:
1- opção w - escrever
2 - opção a - append
3 - opção r - read
'''

with open('4-ManipulandoArquivos/nomes.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(f'Olá, {line.rstrip()}')