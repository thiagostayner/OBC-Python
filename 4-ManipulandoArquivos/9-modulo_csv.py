import csv

cursos = []

with open('4-ManipulandoArquivos/dados/cursos.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursos.append({'language':row['language'], 'category':row['category']})

for curso in sorted(cursos, key=lambda curso: curso['language'], reverse=True):
    print(f'{curso["language"]}-{curso["category"]}')
