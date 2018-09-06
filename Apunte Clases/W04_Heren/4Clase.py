class A:
    atributo_clase = 1

    def __init__(self, parametro):
        self.atributo_instancia = parametro

    def metodo_instancia(self, parametro):
        self.atributo_instancia += parametro
        print(self.atributo_instancia)

objeto_1 = A(4)
objeto_1.metodo_instancia(3)
objeto_1.atributo_clase += 3
print(objeto_1.atributo_clase)
objeto_2 = A(4)
objeto_2.metodo_instancia(3)
print(objeto_2.atributo_clase)
A.atributo_clase += 1
print(A.atributo_clase)
objeto_3 = A(4)
print(objeto_3.atributo_clase)