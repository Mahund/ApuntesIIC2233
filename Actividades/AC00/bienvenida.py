"""Modulo dedicado al inicio del curso IIC2233"""
from math import pi as pi_value
print("Bienvenid@ a IIC2233")


class Circulo:
    """Clase Circulo obtiene coordenadas x e y
    de su centro ademas de su radio"""
    def __init__(self, x_cord, y_cord, radio):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.radio = float(radio)

    def obtener_area(self):
        """Metodo para obtener area del Cuadrado"""
        return pi_value*(self.radio**2)

    def obtener_perimetro(self):
        """Metodo para obtener perimetro del Cuadrado"""
        return 2*pi_value*self.radio

    def __str__(self):
        return f"""Circulo con:
        area = {self.obtener_area()}
        Perimetro = {self.obtener_perimetro()}"""


class Rectangulo:
    """Clase Rectangulo obtiene coordenadas x e y
    de su esquina inferior izquierda ademas de
    su ancho y largo"""
    def __init__(self, x_cord, y_cord, ancho, largo):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.ancho = float(ancho)
        self.largo = float(largo)

    def obtener_area(self):
        """Metodo para obtener area del Rectangulo"""
        return self.largo*self.ancho

    def obtener_perimetro(self):
        """Metodo para obtener perimetro del Rectangulo"""
        return 2*self.largo+2*self.ancho

    def es_cuadrado(self):
        """Metodo para obtener forma del Rectangulo"""
        if self.ancho == self.largo:
            return True
        return False

    def __str__(self):
        if self.es_cuadrado():
            return f"""Cuadrado con:
            area = {self.obtener_area()}
            Perimetro = {self.obtener_perimetro()}"""
        return f"""Rectangulo con:
        area = {self.obtener_area()}
        Perimetro = {self.obtener_perimetro()}"""


if __name__ == "__main__":
    PRIMER_RECTANGULO = Rectangulo(0, 0, 2, 2)
    PRIMER_CIRCULO = Circulo(0, 0, 3)
    print(PRIMER_CIRCULO)
    print(PRIMER_RECTANGULO)
