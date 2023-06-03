'''O encapsulamento é um conceito importante na programação orientada a objetos que visa ocultar os detalhes internos de uma classe e fornecer
uma interface controlada para interagir com os objetos. Ele é implementado por meio da manipulação de níveis de acesso aos atributos e métodos de uma classe.'''

class ContaBanco:
    def __init__(self, nome, saldo):
        self.__nome = nome
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print('saldo insuficiente.')
    
    def extrato(self):
        return self.__saldo
    

conta = ContaBanco("Gabriel", 2000)

print(conta.extrato())

conta.depositar(500)
conta.sacar(200)

print(conta.extrato())
