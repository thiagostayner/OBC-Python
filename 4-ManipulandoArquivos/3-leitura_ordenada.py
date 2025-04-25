nomes = []

with open('4-ManipulandoArquivos/nomes.txt', 'r', encoding='utf') as file:
    for line in file:
        nomes.append(line.rstrip())

organizado = sorted(nomes)

for i in organizado:
    print(f'Olá, {i}')
