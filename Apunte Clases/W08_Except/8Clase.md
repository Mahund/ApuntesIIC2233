04-10-2018

## Exceptions y Testing
_By: Mahund_

#### Introduccion:

- Dudas varias

#### Manejo de excepciones:

- Uso de try, except, else, finally

    1. `try`: intenta correr codigo sin que se levante un error (parte del codigo que podria fallar)

    1. `except`: corre codigo si en try fue levantado cierto error

    1. `else`: si ningun except se corre (codigo que sabemos que no se caera)

    1. `finally`: siempre se corre (incluso si en try hay un return y estamos dentro de una funcion)

#### Lanzar excepciones:

- Se utiliza sentencia `raise`

#### Testing:

```python
import unittest
class MiPrimerTest(unittest.TestCase):

    def test_hello(self):
        expected_output = 3
        self.assertEqual(funcion(), expected_output)


unittest.main()
```

- Revisar resumen de Testing