'''Herança'''

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def Acelerar(self):
        print(f'{self.modelo} Acelerando')

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        Veiculo. __init__(self, marca, modelo)
        self.cor = cor

meu_carro = Carro("Chevrolet", "Onix", 'Prata')

print(meu_carro.cor)
meu_carro.Acelerar()

