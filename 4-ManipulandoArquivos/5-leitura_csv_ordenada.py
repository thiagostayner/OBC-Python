cursos = []

with open('4-ManipulandoArquivos/dados/cursos.csv', 'r', encoding='utf-8') as file:
    for line in file:
        language, category = line.rstrip().split(',')
        cursos.append(f'{language} -{category}')

for curso in sorted(cursos):
    print(curso)