"Back-end module"
# Acá va lo relacionado con el procesamiento de datos
from PyQt5.QtCore import QObject, pyqtSignal, QRect


class CountChecker(QObject):
    """Clase que se encargara de chequear la cuenta del contador."""

    check_signal = pyqtSignal(bool)

    def __init__(self, parent):
        super().__init__()

        # Se conecta la señal check_signal con la función open_window del paren
        # (MainWindow).
        self.check_signal.connect(parent.open_window)

    def check(self, string):
        """
        Función que chequea que la cuenta no supere 5. en el caso de superarlo,
        envia una señal
        True al frontend.
        :param count: str
        :return: none
        """
        if len(string) > 6 and string.isalpha():
            self.check_signal.emit(True)
        else:
            self.check_signal.emit(False)


class Character(QObject):

    update_position_signal = pyqtSignal(dict)

    def __init__(self, parent, x, y):
        super().__init__()
        self.jumping = False
        self.direction = 'R'
        self._x = x
        self._y = y
        self.padre = parent

        # Se conecta la señal update_position con el metodo
        # del parent (MainGame.update_position)
        self.update_position_signal.connect(parent.update_position)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        """
        Envía la señal update_position al cambiar la coordenada y.
        :param value: int
        :return: none
        """
        if 8 < value < 590:
            self._y = value
            self.update_position_signal.emit({'x': self.x, 'y': self.y})
            self.check_collisions()

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        """
        Chequea que la coordenada x se encuentre dentro de
        los parámetros y envía la señal
        update_position con las nuevas coordenadas.
        :param value: int
        :return: none
        """
        if 2 < value < 532:
            self._x = value
            self.update_position_signal.emit({'x': self.x, 'y': self.y})
            self.check_collisions()

    def move(self, event):
        """
        Función que maneja los eventos de movimiento (L, R) y de salto.
        :param event: str
        :return: none
        """
        if event == 'R':
            self.x += 10
            self.direction = 'R'
        if event == 'L':
            self.x -= 10
            self.direction = 'L'
        if event == 'U':
            self.y -= 10
            self.direction = 'U'
        if event == 'D':
            self.y += 10
            self.direction = 'D'

    def check_collisions(self):
        yo = QRect(self.x, self.y, 20, 20)
        for fruta in self.padre.frutas:
            frutita = QRect(fruta[1]._x, fruta[1]._y, 5, 5)
            if yo.intersects(frutita):
                fruta[0].hide()



class Fruit(QObject):

    def __init__(self, parent, x, y):
        super().__init__()
        self._x = x
        self._y = y
