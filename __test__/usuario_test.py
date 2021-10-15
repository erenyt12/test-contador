import unittest
from juampi.usuario import Usuario\

class TestUsuario(unittest.TestCase):
    def setUp(self) -> None:
        self.juampi = Usuario("Juampi")

    def test_elContadorDelUsuarioInicializaEnCero(self):      
        self.assertEqual(self.juampi.contador.valor, 0)

    def test_incrementarElContadorDelUsuario(self):
        self.assertEqual(self.juampi.contador.valor, 0)

        self.juampi.incrementarContador()

        self.assertEqual(self.juampi.contador.valor, 1)


    def test_decrementarElContadorDelUsuario(self):
        self.juampi.incrementarContador()

        self.assertEqual(self.juampi.contador.valor, 1)

        self.juampi.decrementarContador()

        self.assertEqual(self.juampi.contador.valor, 0)



if __name__ == "__main__":
    unittest.main()