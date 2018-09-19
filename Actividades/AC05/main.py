# Aqui abajo debes escribir el código de tus clases
from abc import ABC, abstractmethod


class Ser(ABC):
    "Clase abstracta Ser"
    def __init__(self, nombre, fuerza, resistencia, vida, ki, *args, **kwargs):
        # print(args, kwargs)
        super().__init__(*args, **kwargs)
        self.nombre = nombre
        self.fuerza = fuerza
        self.resistencia = resistencia
        self._vida = vida
        self.ki = ki

    @property
    def vida(self):
        "Getter"
        return self._vida

    @vida.setter
    def vida(self, value):
        "Setter"
        self._vida = max(value, 0)
        # self._vida = value
        # if self._vida < 0:
        #    self._vida = 0

    @abstractmethod
    def atacar(self, enemigo):
        "Metodo abstracto de atacar"
        pass


class Humano(Ser):
    "Clase Humano"
    def __init__(self, *args, inteligencia=100, **kwargs):
        # print("himano", *args, inteligencia, **kwargs)
        super().__init__(*args, **kwargs)
        self.inteligencia = inteligencia

    def atacar(self, enemigo):
        "Atacar"
        vida_perdida = max(self.ki*(1+self.fuerza-enemigo.resistencia)/2, 0)
        print(f"{self.nombre} le quita {vida_perdida}\
 de vida a {enemigo.nombre}")
        enemigo.vida -= vida_perdida

    def meditar(self):
        "Meditar"
        print(f"Yo {self.nombre} estoy meditando!")
        self.ki += self.inteligencia/100


class Extraterrestre(Ser):
    "Clase Extraterrestre"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def atacar(self, enemigo):
        "Atacar"
        vida_perdida = max(self.ki*(1+self.fuerza-enemigo.resistencia), 0)
        enemigo.vida -= vida_perdida
        self.fuerza *= 1.3
        print(f"{self.nombre} le quita {vida_perdida}\
 de vida a {enemigo.nombre}")


class Supersaiyayin(Extraterrestre, Humano):
    "Clase Supersaiyayin"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cola = True

    def perder_cola(self):
        "Si tiene cola la elimina"
        if self.cola:
            self.cola = False
            self.resistencia *= 0.4


class Hakashis(Extraterrestre):
    "Clase Hakashis"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def robarki(self, *adversarios):
        "Robar ki"
        for rival in adversarios:
            rival.ki *= 0.5
            self.ki += rival.ki


if __name__ == '__main__':
    """
    A continuación debes instanciar cada uno de los objetos pedidos,
    para que puedas simular la batalla.

    nombre, fuerza, resistencia, vida, ki
    """
    YO = Humano("Micha", 1.2, 0.8, 30, 1.5, inteligencia=80)
    TU = Supersaiyayin("Nebil", 1.3, 1.2, 50, 2)
    SENSEI = Supersaiyayin("Goku", 2, 2, 90, 4)
    OMAE = Hakashis("Wa", 1.5, 1.5, 90, 3)
    MOU = Hakashis("Shindeiru", 1.5, 1.5, 90, 3)
    JAVI = Supersaiyayin("Nymeria", 3.5, 2.1, 33, 7)
    YO.atacar(TU)
    JAVI.atacar(YO)
