"Modulo dedicado a la activida 04"


class Aventurero:
    "Clase abstracta"
    def __init__(self, nombre, vida, ataque, velocidad):
        self.nombre = nombre
        self._vida = float(vida)
        self._ataque = float(ataque)
        self._velocidad = float(velocidad)

    @property
    def poder(self):
        "Poder getter"
        return self._vida+self._ataque+self._velocidad

    @property
    def vida(self):
        "Vida getter"
        return self._vida

    @vida.setter  # sorted((0, value, 100))[1]
    def vida(self, value):
        self._vida = float(value)
        if self._vida < 0:
            self._vida = 0.0
        elif self._vida > 100:
            self._vida = 100.0

    def grito_de_guerra(self):
        "Grito de guerraaaaaa"
        return f"{self.nombre}: ¡Gloria al gran Tini!"

    def __repr__(self):
        return f"Nombre: {self.nombre}, poder: {self.poder}"


class Guerrero(Aventurero):
    "Hereda de aventurero"
    def __init__(self, defensa, **kwargs):
        super().__init__(**kwargs)
        self._defensa = float(defensa)

    @property
    def poder(self):
        a_val = (0.8 * self._vida) + (2.2 * self._ataque)
        b_val = (1.5 * self._defensa) + (0.5 * self._velocidad)
        return a_val+b_val


class Mago(Aventurero):
    "Hereda de aventurero"
    def __init__(self, magia, **kwargs):
        super().__init__(**kwargs)
        self._magia = float(magia)

    @property
    def poder(self):
        a_val = (1.0 * self._vida) + (0.1 * self._ataque)
        b_val = (2.5 * self._magia) + (1.4 * self._velocidad)
        return a_val+b_val


class Monstruo:
    "Clase monstruo: buaaaaaa"
    def __init__(self, nombre, vida, poder, jefe):
        self.nombre = nombre
        self._vida = float(vida)
        self._poder = float(poder)
        self._jefe = jefe

    @property
    def poder(self):
        "Poder si es jefe"
        if self._jefe:
            return 3*self._poder
        return self._poder

    @property
    def vida(self):
        "Vida getter"
        return self._vida

    @vida.setter  # sorted((0, value, 100))[1]
    def vida(self, value):
        self._vida = float(value)
        if self._vida < 0:
            self._vida = 0.0

    def __repr__(self):
        return f"Nombre: {self.nombre}, poder: {self.poder}"


class Clan:
    "Clan"
    valor_clan = {"Bronce": 0.5, "Plata": 0.75, "Oro": 1.2}
    instancia_permitida = {"<class '__main__.Clan'>": Aventurero,
                           "<class '__main__.Mazmorra'>": Monstruo}

    def __init__(self, nombre, miembros=None):
        self.nombre = nombre
        if not miembros:
            self._miembros = list()
        else:
            self._miembros = miembros

    @property
    def rango(self):
        "Rango getter"
        if len(self._miembros) < 3:
            return "Bronce"
        if len(self._miembros) < 6:
            return "Plata"
        return "Oro"

    @property
    def poder(self):
        "Poder getter"
        return sum([ser.poder * Clan.valor_clan[self.rango]
                    for ser in self._miembros])

    def agregar(self, entidad):
        "Agregarlos"
        if isinstance(entidad, CLAN.instancia_permitida[str(type(self))]):
            self._miembros.append(entidad)
            print(f"Agregado {entidad.nombre} a {self.nombre}")
        else:
            print(f"Entidad invalida!, no corresponde a \
{CLAN.instancia_permitida[str(type(self))]}")

    def remover(self, entidad):
        "eliminando"
        if entidad in self._miembros:
            self._miembros.pop(self._miembros.index(entidad))
            print(f"Se ha removido a {entidad.nombre}")
        else:
            print(f"Entidad {entidad.nombre} no encontrada")

    def __repr__(self):
        return f"Nombre: {self.nombre}, poder: {self.poder}\
rango: {self.rango}, miembros: {len(self._miembros)}"


class Mazmorra(Clan):
    "Mazmorra"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def poder(self):
        return sum([ser.poder for ser in self._miembros])

    def __repr__(self):
        return f"Nombre: {self.nombre}, poder: {self.poder}"


if __name__ == "__main__":
    YO = Aventurero(nombre="Micha", vida=50, ataque=50,
                    velocidad=20)
    YO.vida -= 10
    print(YO.vida)
    TU = Guerrero(nombre="Stefan", vida=10, ataque=20,
                  velocidad=30, defensa=40)
    OTRO = Mago(nombre="Stefan", vida=10, ataque=20,
                velocidad=30, magia=40)
    CLAN = Clan(nombre="Clan Los poderosos", miembros=[YO, TU])

    MOSTRUE = Monstruo(nombre="Nebil", vida=10, poder=100, jefe=True)

    print(CLAN.poder)
    CLAN.agregar(Monstruo("micha", 10, 10, False))
    CLAN.agregar(OTRO)
    CLAN.remover(YO)
    CLAN.remover(YO)
    MAZMORRA = Mazmorra(nombre="Mazmorra Kawas", miembros=[])
    MAZMORRA.agregar(YO)
    MAZMORRA.agregar(MOSTRUE)
