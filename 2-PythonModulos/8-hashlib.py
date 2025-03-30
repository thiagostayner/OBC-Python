import hashlib

# 1 - verificar os algoritmos disponíveis
print(hashlib.algorithms_available)

# 2 - Os algoritmos disponíveis de acordo com o SO
print(hashlib.algorithms_guaranteed)

# 3 - Utilizando o Sha256
algoritimo = hashlib.sha256()
print(algoritimo.digest())
mensagem = 'A melhor forma de prever o futuro é criá-lo'.encode()
algoritimo.update(mensagem)
print(algoritimo.hexdigest())

# 4 - utilizando o md5
md5 = hashlib.md5()
md5.update(mensagem)
print(md5.hexdigest())