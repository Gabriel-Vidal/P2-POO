'''Herança é um conceito fundamental na programação orientada a objetos (POO) que permite criar novas classes (subclasses) com base em classes existentes (superclasses).
Na herança, a classe filha (subclasse) herda os atributos e métodos da classe pai (superclasse), possibilitando reutilizar o código e estabelecer uma relação de especialização
entre as classes.'''

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

