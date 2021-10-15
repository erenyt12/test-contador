import unittest
from juampi.contador import Contador

class TestContador(unittest.TestCase):
    def setUp(self) -> None:
        self.contador = Contador()

    def test_elContadorInicializaEnCero(self):      
        self.assertEqual(self.contador.valor, 0)

    def test_contadorIncrementaSuValorEnUno(self):
        self.assertEqual(self.contador.valor, 0 )

        self.contador.incrementar()

        self.assertEqual(self.contador.valor, 1 )


    def test_contadorDecrementaSuValorEnUno(self):
        self.contador.incrementar()

        self.assertEqual(self.contador.valor, 1 )

        self.contador.decrementar()

        self.assertEqual(self.contador.valor, 0)




if __name__ == "__main__":
    unittest.main()