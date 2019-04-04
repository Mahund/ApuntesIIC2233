"Front-end module"
# Acá va lo relacionado con la GUI.
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, Qt
from random import randint
from backend import CountChecker, Character, Fruit


class MainWindow(QWidget):

    check_count_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 300, 300)

        self.name_label = QLineEdit('', self)
        self.contador_label = QLabel('Ingresa tu usuario en la \
ventana superior', self)
        self.main_game_button = QPushButton('Inicio', self)

        # Se conecta el boton con la función check_count
        self.main_game_button.clicked.connect(self.check_count)

        # Se Instancia el CountChecker.
        self.spell_checker = CountChecker(self)
        self.check_count_signal.connect(self.spell_checker.check)

        vbox = QVBoxLayout()
        vbox.addWidget(self.name_label)
        vbox.addWidget(self.contador_label)
        vbox.addWidget(self.main_game_button)
        self.setLayout(vbox)

    def check_count(self):
        """
        Función que incrementa el contador y envía una
        señal al CheckCount con la cuenta.
        También actualiza el label del contador.
        :return: none
        """
        self.check_count_signal.emit(self.name_label.text())

    def open_window(self, state):
        """
        Función que dado un estado, cambia la ventana de inicio por ladeljuego
        :param state: bool
        :return: none
        """
        if state:
            self.hide()
            self.maingame = MainGame()
            self.maingame.show()
        else:
            self.contador_label.setText("Usuario invalido, intenta denuevo")


class MainGame(QWidget):
    "Docsting"

    move_character_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 560, 615)
        self._frame = 1
        self.frutas = list()

        # Se setea la imagen de fondo.
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap('sprites/map.png'))

        # Se instancia el personaje del backend y se
        # conecta move_character_signal con la función
        # move de Character.
        self.backend_character = Character(self, 280, 300)
        self.move_character_signal.connect(self.backend_character.move)

        # Se crea el personaje en el frontend.
        self.front_character = QLabel(self)
        self.front_character.setPixmap(QPixmap('sprites/pacman_R_2'))
        self.front_character.move(280, 300)

    @property
    def frame(self):
        return self._frame

    @frame.setter
    def frame(self, value):
        if value > 3:
            self._frame = 1
        else:
            self._frame = value

    def keyPressEvent(self, e):
        """
        Dada la presión de una tecla se llama a esta función.
        Al apretarse una tecla chequeamos si
        esta dentro de las teclas del control del juego y de ser así,
        se envía una señal al backend
        con la acción además de actualizar el sprite.
        :param e: QKeyEvent
        :return:
        """
        self.frame += 1
        if e.key() == Qt.Key_D:
            self.front_character.setPixmap(QPixmap(f'sprites/\
pacman_R_{self.frame}.png'))
            self.move_character_signal.emit('R')
        if e.key() == Qt.Key_A:
            self.front_character.setPixmap(QPixmap(f'sprites/\
pacman_L_{self.frame}.png'))
            self.move_character_signal.emit('L')
        if e.key() == Qt.Key_W:
            self.front_character.setPixmap(QPixmap(f'sprites/\
pacman_U_{self.frame}.png'))
            self.move_character_signal.emit('U')
        if e.key() == Qt.Key_S:
            self.front_character.setPixmap(QPixmap(f'sprites/\
pacman_D_{self.frame}.png'))
            self.move_character_signal.emit('D')
        if e.key() == Qt.Key_Space:
            self.crear_fruta()

    def crear_fruta(self):
        coord_x = randint(18, 540)
        coord_y = randint(14, 593)
        backend_fruit = Fruit(self, coord_x, coord_y)

        # Se crea el pearsonaje en el frontend.
        front_fruit = QLabel(self)
        front_fruit.setPixmap(QPixmap('sprites/cherry.png'))
        front_fruit.move(coord_x, coord_y)
        front_fruit.show()
        self.frutas.append((front_fruit, backend_fruit))

    def update_position(self, event):
        """
        Función que recibe un diccionario con las
        cordenadas del personaje y las actualiza en el
        frontend.
        :param event: dict
        :return: none
        """
        self.front_character.move(event['x'], event['y'])


if __name__ == '__main__':
    app = QApplication([])
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
