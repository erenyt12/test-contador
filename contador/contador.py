class Contador(object):
    def __init__(self) -> None:
        self.__valor = 0

    @property
    def valor(self): return self.__valor

    # @valor.setter
    # def valor(self, un_valor):  self.__valor = un_valor

    def incrementar(self): self.__valor += 1
    def decrementar(self): self.__valor -= 1

if __name__ == "__main__":
    contador = Contador()

    print(contador.valor)

    contador.valor = 3

    print(contador.valor)