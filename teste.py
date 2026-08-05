class ContaBancaria:
    def __init__(self):
        self.__saldo = 0

    def depositar(self,valor):
        self.__saldo += valor

    def get_saldo(self):
        return self.__saldo

c1 = ContaBancaria()
c1.depositar(100)
print(c1.get_saldo())