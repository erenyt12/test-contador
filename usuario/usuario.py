from contador import Contador

class Usuario(object):
    def __init__(self, nombre) -> None:
        self.__nombre = nombre
        self.__contador = Contador()

    
    @property
    def nombre(self): return self.__nombre
    @property
    def contador(self): return self.__contador

    def incrementarContador(self): self.contador.incrementar()
    def decrementarContador(self): self.contador.decrementar()

if __name__ == "__main__":
    usuario = Usuario("Jumapi")

    print(usuario.nombre)
