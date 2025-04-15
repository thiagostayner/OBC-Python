class Telefone:
    def __init__(self, brand, modelo, preco):
        self._brand = brand
        self._modelo = modelo
        self._preco = preco

    def __str__(self):
        return f'{self._brand} {self._modelo}'
    
    @staticmethod
    def fazer_ligacao(num_telefone):
        print(f'ligando para {num_telefone}')

    def disconto(self):
        return self._preco * 0.10

class Celular(Telefone):
    def __init__(self, brand, modelo, preco, ram, memoria, camera_traseira):
        super().__init__(brand, modelo, preco)

        self.ram = ram
        self.memoria = memoria
        self.camera_traseira = camera_traseira

    def disconto(self):
        return self._preco * 0.15

Moto = Telefone('Moto', 'G7', 1000)
print(Moto)
Moto.fazer_ligacao(1312322)
print(f'Valor do  {Moto._brand} {Moto._modelo} é {Moto._preco}')
print(vars(Moto))
print(Moto.disconto())

Iphone = Celular('Iphone', '13', 5000, '4GB', '128GB', '25MP')
Iphone.fazer_ligacao(2433534)
print(f'Valor do  {Iphone._brand} {Iphone._modelo} é {Iphone._preco}')
print(vars(Iphone))
print(Iphone.disconto())