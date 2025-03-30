import json

# 1 - converter strings para dicionários
pessoa = '{"nome":"Rodrigo", "linguas":["Python", "Javascript"]}'
pessoa_dicionario = json.loads(pessoa)
print(pessoa_dicionario)
print(pessoa_dicionario['linguas'])

# 2 - converter dicionário para json
pessoa_json = json.dumps(pessoa_dicionario)
print(pessoa_json)
print(type(pessoa_json))
print(type(pessoa_dicionario))

# 3 - formatando json
print(json.dumps(pessoa_dicionario, indent=4, sort_keys=True))

# 4 - salvando json em txt
with open('person.txt', 'w') as json_file: # w significa write, para criar arquivo novo
    json.dump(pessoa_dicionario, json_file)

# 5 - lendo json externo
with open('iris.json', 'r') as f:
    data = json.load(f)
    print(data)