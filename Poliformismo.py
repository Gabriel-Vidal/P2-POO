'''Polimorfismo é um conceito da programação orientada a objetos (POO) que permite que um objeto seja tratado de diferentes formas, dependendo do contexto em que é utilizado.
Em outras palavras, é a capacidade de um objeto de ser referenciado e utilizado como uma instância de sua classe base ou como uma instância de uma de suas subclasses.'''

class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au Au"
    

class Gato(Animal):
    def falar(self):
        return "Miau"
    

def fazer_barulho(animal):
    print(animal.falar())


cachorro = Cachorro()
gato = Gato()

fazer_barulho(cachorro)
fazer_barulho(gato)