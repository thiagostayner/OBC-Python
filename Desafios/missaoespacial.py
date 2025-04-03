'''
A Missão Espacial dos Bits Perdidos 🚀
Bem-vindo, bravo programador! Você foi convocado para uma missão extremamente importante pela Agência Espacial dos Programadores. Recentemente, captamos um sinal misterioso vindo de uma galáxia distante, que parece conter informações valiosas sobre uma tecnologia alienígena crucial para a humanidade.

Porém, durante a transmissão através dos confins do universo, os dados foram embaralhados! 😱 Sua missão, caso você escolha aceitá-la, é decifrar essa mensagem.

🖧 Descrição da Missão
Você receberá uma string especial, que representa os dados recebidos do espaço. Esta string contém apenas zeros e uns, mas a ordem das informações foi invertida por um pulso eletromagnético misterioso.

Seu objetivo é inverter a string para restaurar a mensagem original!

Instruções
Escreva uma função chamada decode_sinal que recebe um único parâmetro, uma string composta apenas por '0' e '1'.
A função deve retornar a string na ordem inversa.
Exemplo
Entrada: '1101001'
Saída esperada: '1001011'
Pegue seu traje espacial e prepare-se para decifrar o código cósmico dos bits perdidos! Boa sorte, astronauta dos algoritmos! 👩‍🚀💻🚀
'''

def decode_sinal(string):
    string = str(input())
    string_inversa = string[::-1]
    return string_inversa

print(decode_sinal())