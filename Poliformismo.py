'''Polimorfismo'''

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