import csv

name = input('Informe o nome da linguagem que deseja aprender: ')
category = input('Qual a categoria que a linguagem se encaixa? ')

with open ('4-ManipulandoArquivos/dados/cursos.csv', 'a', encoding='utf-8') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerow([name, category])