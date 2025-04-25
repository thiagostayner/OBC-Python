import glob, os, zipfile

# glob acesso a informações, conseguir listar arquivo dentro do diretorio
# os modulo de sistema operacional
# zipfile compactar arquivos .zip

# 1 - Diretorio de trabalho atual
os.getcwd()

# 2 - Listar todos os arquivos txt
for file in glob.glob('4-ManipulandoArquivos/dados/*.txt'):
    print(file)

# 3 - Listar todos os arquivos .csv
for file in glob.glob('4-ManipulandoArquivos/dados/*.csv'):
    print(file)

# 4 - Compactar arquivos .txt
with zipfile.ZipFile('names.zip', 'w') as zip:
    for file in glob.glob('4-ManipulandoArquivos/dados/*.txt'):
        zip.write(file)

# 5 - Compactar arquivos .csv
with zipfile.ZipFile('cursos.zip', 'w') as zip:
    for file in glob.glob('4-ManipulandoArquivos/dados/*.csv'):
        zip.write(file)

# 6 - Compactar todos os arquivos
with zipfile.ZipFile('code.zip', 'w') as zip:
    for file in glob.glob('4-ManipulandoArquivos/*'):
        zip.write(file)