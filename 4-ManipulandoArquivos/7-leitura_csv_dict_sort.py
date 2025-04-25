cursos = []

with open('4-ManipulandoArquivos/dados/cursos.csv', 'r', encoding='utf-8') as file:
    for line in file:
        language, category = line.rstrip().split(',')
        curso = {}
        curso['language'] = language
        curso['category'] = category
        cursos.append(curso)

print(cursos)

def get_language(curso):
    return curso['language']

def get_category(curso):
    return curso['category']

for curso in sorted(cursos, key=get_language):
    print(f'{curso["language"]} -{curso["category"]}')