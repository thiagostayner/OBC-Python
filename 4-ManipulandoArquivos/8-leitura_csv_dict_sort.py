cursos = []

with open('4-ManipulandoArquivos/dados/cursos.csv', 'r', encoding='utf-8') as file:
    for line in file:
        language, category = line.rstrip().split(',')
        curso = {}
        curso['language'] = language
        curso['category'] = category
        cursos.append(curso)

print(cursos)

for curso in sorted(cursos, key=lambda curso: curso['language']):
    print(f'{curso["language"]} -{curso["category"]}')