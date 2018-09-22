"Modulo actividad 6"
from functools import reduce
from textwrap import indent

ORDEN = {"general": "teniente", "teniente": "mayor",
         "mayor": "capitan", "capitan": "soldado"}


class Entidad:
    "Clase entidad"
    def __init__(self, rango, *items,
                 superior=None, subordinados=None):
        self.rango = rango
        self.items = set(items)
        self.superior = superior
        self.subordinados = subordinados if subordinados else []

    @property
    def superiores(self):
        "Getter"
        aux = self.superior.superiores if self.superior else []
        return (aux + [self.superior]) if self.superior else aux

    @property
    def afinidad_superiores(self):
        "Docstring"
        return sum([self._afinidad(x) for x in self.superiores])

    @property
    def rangos_subordinables(self):
        "Getter rangos"
        if self.rango == "soldado":
            return set()
        return reduce(lambda x, y: x | y,
                      (x.rangos_subordinables for x in self.subordinados),
                      {ORDEN[self.rango]})

    @property
    def poder(self):
        "Poder"
        return sum([nodo.afinidad_superiores for nodo in self])

    def agregar_subordinado(self, entidad):
        "Agregar"
        if entidad.rango == ORDEN[self.rango]:
            self.subordinados.append(entidad)
            entidad.superior = self
        else:
            self.mejor_asignacion(entidad).agregar_subordinado(entidad)

    def mejor_asignacion(self, entidad):
        "Docstring"
        validos = filter(lambda x: entidad.rango in x.rangos_subordinables,
                         self.subordinados)
        return max(validos, key=lambda x: entidad._afinidad(x))

    def _afinidad(self, other):
        "Docstring"
        return len(self.items & other.items)

    def __iter__(self):
        yield self
        for child in self.subordinados:
            yield from child

#     def __str__(self):
#         return f"""
# Rango: {self.rango}
# Superior: {repr(self.superior)}
# Subordinados: {repr(self. subordinados)}\n
#         """

    def __repr__(self):
        # texto = f"Rango: {self.rango}\nItems: {self.items}\n"
        texto = f"Rango: {self.rango}\n"
        texto_sub = [indent(repr(sub), "  ") for sub in self.subordinados]
        return texto + "".join(texto_sub)


if __name__ == "__main__":
    with open(file=f"ejercito_1.csv",
              mode='r', encoding="UTF-8") as file:
        T = Entidad(*file.readline().strip().split(","))
        for linea in file:
            candidato = Entidad(*linea.strip().split(","))
            T.agregar_subordinado(candidato)
        print(T)
