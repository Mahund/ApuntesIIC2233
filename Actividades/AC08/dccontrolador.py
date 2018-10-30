from collections import Counter, namedtuple

###############################################################################
"""
Excepciones Personalizadas
Acá crea tus excepciones personalizadas
"""


class RepeatedError(Exception):
    def __init__(self, texto):
        super().__init__(texto)


class InconsistencyError(Exception):
    def __init__(self, texto):
        super().__init__(texto)
###############################################################################


class Producto:
    def __init__(self, nombre, precio_base, descuento=0):
        self.nombre = nombre
        self.precio_base = precio_base
        if not 0 <= descuento <= 0.5:
            raise ValueError("descuento no esta entre 0% y 50%")
        self.descuento = descuento

    @property
    def precio(self):
        return self.precio_base * (1 - self.descuento)

    @precio.setter
    def precio(self, value):
        if value < 0:
            raise ValueError("precio base menor que 0")
        self.precio_base = value

    def __str__(self):
        porcentaje_descuento = self.descuento * 100
        return f'{self.nombre}: '\
                f'${self.precio_base} ({porcentaje_descuento}% dscto.)'

    def __repr__(self):
        return f'<Producto {self}>'


class Supermercado:
    CARCTERES_INVALIDOS = '-&%#@*()'

    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = {}

    @property
    def productos(self):
        return self.catalogo.values()

    def agregar_producto(self, codigo, producto):
        for letra in str(codigo):
            if letra in "-& %#@*()":
                raise ValueError(f"codigo posee caracter invalido: {letra}")
        if self.catalogo.get(codigo):
            raise RepeatedError(f"{codigo} ya esta siendo utilizado")
        self.catalogo[codigo] = producto

    def __getitem__(self, key):
        return self.catalogo[key]

    def __contains__(self, producto): #Debe retornar un booleando y deberia ser .values()
        return producto in self.catalogo

    def __iter__(self):
        yield from self.catalogo.values()


class PedidoOnline:
    def __init__(self, supermercado, orden=None):
        self.supermercado = supermercado

        # orden puede ser un arreglo de elementos:
        # ['a', 'a', 'b', 'c', 'a', 'b'] => {'a': 3, 'b': 2, 'c': 1}
        # o un dict con los conteos
        # {'a': 3, 'b': 2, 'c': 1} => {'a': 3, 'b': 2, 'c': 1}
        self.orden = Counter(orden)

    def añadir_producto(self, producto, cantidad=1):
        if cantidad < 0:
            raise ValueError("cantidad menor a 0")
        if producto not in self.supermercado.catalogo.values():
            raise KeyError("El producto no existe en el supermercado")
        self.orden[producto] += cantidad

    @property
    def productos(self):
        return self.orden.keys()

    @property
    def total(self):
        return sum(producto.precio * cantidad for producto, cantidad in self)

    def comprar(self, dinero):
        if dinero < self.total:
            print('Falta dinero, la compra no fue exitosa.')
            return

        print(f'Compra exitosa! (El Dr. H^4 aplaude silenciosamente).')
        self.orden.clear()
        return dinero - self.total  # vuelto

    def __add__(self, other):
        if self.supermercado is not other.supermercado:
            raise InconsistencyError("carros de compra de\
distintos supermercados")
        nueva_orden = self.orden + other.orden

        return PedidoOnline(self.supermercado, nueva_orden)

    def __iter__(self):
        yield from self.orden.items()

    def __contains__(self, producto):
        return producto in self.orden


if __name__ == "__main__":
    PROD = Producto("nombre", 10, 0.2)
    PROD2 = Producto("nombre", 10, 0.2)
    SUPE = Supermercado("Las Lias")
    SUPE2 = Supermercado("Las Violas")
    PEDI = PedidoOnline(SUPE)
    PEDI2 = PedidoOnline(SUPE2)
    SUPE.agregar_producto(1, PROD)
    # PEDI+PEDI2
    # SUPE.agregar_producto(1, PROD2)
    # PEDI.añadir_producto(PROD2)
