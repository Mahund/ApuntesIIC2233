14:30 03-10-2018

## Testing
_By: Mahund_

#### Introduccion:

- Codigo capaz de poner a prueba diferentes programas, automatizando las pruebas *manuales* que normalmente se realizaban.

- Si un programa no va de la mano con un programa que lo testee, ya que si no esta testeado poseerá **bugs**
> Untested code is broken code

#### Pruebas unitarias:

- Encargadas de *verificar* unidades minimas del codigo.

- Las más utilizadas son `pytest` y `unittest`

##### unittest:

- Las clases creadas deben heredar de `TestCase`

- Por convencion los metodos de estas clases **deben** iniciar con *test*
    ```python
    import unittest

    class ChequearNumeros(unittest.TestCase):
        # este test debería funcionar
        def test_int_float(self):
            self.assertEqual(1, 1.0)
     
        # este test debería fallar    
        def test_str_float(self):
            self.assertEqual(1, "1")
    # Si quisiéramos ejecutar el test por consola:
    if __name__ == "__main__":
       unittest.main()
    # Si no quisieramos ejecutarlo por consola:
    suite = unittest.TestLoader().loadTestsFromTestCase(ChequearNumeros)
    unittest.TextTestRunner().run(suite)
    ```

- "." indica test pasados, "F" indica test fallado

- Cada test debe ser **independiente** de los otros 

##### Metodos de asercion:

1. self.assertEqual([1, 2, 3], [1, 2, 3])
> falla si a != b
1. self.assertNotEqual("hola", "chao")
> falla si a == b
1. self.assertTrue("Hola" == "Hola")
> falla si bool(x) es False
1. self.assertFalse("Hola" == "Chao")
> falla si bool(x) es True
1. self.assertIs(a, b)
> falla si a no es b
1. self.assertIsNot(a, c)
> falla si a es b.  
> Notar que "is" implica igualdad (==), pero no al revés, dos objetos distintos pueden tener el mismo valor.    
1. self.assertIsNone(None)
> falla si x no es None
1. self.assertIsNotNone(2)
> falla si x es None
1. self.assertIn(2, [2, 3, 4])
> falla si a no está en b
1. self.assertNotIn(1, [2, 3, 4])
> falla si a está en b
1. self.assertIsInstance("Hola", str)
> falla si isinstance(a, b) es False
1. self.assertNotIsInstance("1", int)
> falla si isinstance(a, b) es True
1. self.assertRaises (excepcion, callable, args)
> falla si callable con args como parametros no levanta excepcion esperada
1. self.assertAlmostEqual(first, second, places=7, msg=None, delta=None)
> Testea que first y second sean aproximadamente iguales, calculando la diferencia, redondeando al número dado de decimales (por defecto son 7). Si se provee el argumento delta en vez de places, la diferencia entre first y second debe ser menor o igual (o mayor en el caso de assertNotAlmostEqual) que delta.

##### Metodo setUp y tearDown:

- `setUp`: permite declarar las variables que serán usadas para los tests, se ejecuta antes de cada una de las pruebas.

- `tearDowb`: permite *limpiar* una vez terminado los test, por ej si algun test creo un archivo este metodo lo borrara 

    ```python
    from collections import defaultdict
    import unittest
    import os


    class ListaEstadisticas(list):
        def media(self):
            return sum(self) / len(self)
        
        def mediana(self):
            if len(self) % 2:
                return self[int(len(self) / 2)]
            else:
                idx = int(len(self) / 2)
                return (self[idx] + self[idx-1]) / 2
            
        def moda(self):
            freqs = defaultdict(int)
            for item in self:
                freqs[item] += 1
            moda_freq = max(freqs.values())
            modas = []
            for item, value in freqs.items():
                if value == moda_freq:
                    modas.append(item)
            return modas


    class TestearEstadisticas(unittest.TestCase):
        
        def setUp(self):
            self.stats = ListaEstadisticas([1, 2, 2, 3, 3, 4])
            self.archivo_temporal = open("algo.txt", "w")

        def tearDown(self):
            self.archivo_temporal.close()
            os.remove("algo.txt")
            
        def test_media(self):
            print(self.stats)
            self.assertEqual(self.stats.media(), 2.5)
            
        def test_mediana(self):
            self.assertEqual(self.stats.mediana(), 2.5)
            self.stats.append(4) # Alterar stats definidos en setUp no altera la variable para test siguientes
            self.assertEqual(self.stats.mediana(), 3)
            
        def test_moda(self):
            print(self.stats)
            self.assertEqual(self.stats.moda(), [2, 3])
            self.stats.remove(2)
            self.assertEqual(self.stats.moda(), [3])
                    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestearEstadisticas)
    unittest.TextTestRunner().run(suite)
    ```

#### Organizar los test:

- Podemos organizar los módulos que contienen tests (objetos TestCase) en módulos más generales llamados test suites (objetos TestSuite).

    ```python
    class TestAritmetico(unittest.TestCase):

        def test_arit(self):
            self.assertEqual(1+1,2)

    class TestAritmetico2(unittest.TestCase):

        def test_arit2(self):
            self.assertNotEqual(2*1,1)
            
    Tsuite = unittest.TestSuite()
    Tsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAritmetico))
    Tsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAritmetico2))
    unittest.TextTestRunner().run(Tsuite)
    ```

#### Ignorar test fallidos:

- Hay algunos casos en que sabremos que ciertos test fallaran (funciones inconclusas, etc)

    ```python
    import unittest
    import sys

    class IgnorarTests(unittest.TestCase):
        
        # Este test fallará
        def test_que_no_sabiamos_que_falla(self):
            self.assertEqual(False, True)
        
        @unittest.expectedFailure
        def test_sabemos_que_falla(self):
            self.assertEqual(False, True)
            
        @unittest.skip("Test inútil")
        def test_ignorar(self):
            self.assertEqual(False, True)
            
        @unittest.skipIf(sys.version_info.minor < 5, "No funciona en Python 3.1.")
        def test_ignorar_if(self):
            self.assertEqual(False, True)
            
        @unittest.skipUnless(sys.platform.startswith("linux"), "No funciona, a excepción de Linux.")
        def test_ignorar_unless(self):
            self.assertEqual(False, True)
        

                            
    suite = unittest.TestLoader().loadTestsFromTestCase(IgnorarTests)
    unittest.TextTestRunner().run(suite)
    ```