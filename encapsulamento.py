'''Encapsulamento'''

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
