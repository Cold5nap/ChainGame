from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject

from graphics.uiV2 import Ui_MainWindow
from logic.game import Level, Color, FigureType


# table_view сделать
# индексы матрицы логики соответствуют индексам строки от sender
class GrBoard(QMainWindow):
    def __init__(self, board: Level):
        super(GrBoard, self).__init__()
        ui = Ui_MainWindow()
        ui.setupUi(self)
        self.ui = ui
        self.but_matrix = [[], [], []]
        self.board = board

        self.add_buttons()
        self.set_icon_to_buttons()
        self.set_actions()

    def set_actions(self):
        b: QtWidgets.QPushButton
        for b in self.but_matrix:
            a = 1
            # b.clicked.connect(self.action_clicked)

    @pyqtSlot()
    def action_clicked(self):
        double_index = self.sender().text()
        print(double_index, self.but_matrix[0][0].text())
        row = int(double_index[0])
        col = int(double_index[1])

    def load_icon(self, figure, button: QtWidgets.QPushButton):
        icon = QtGui.QIcon()
        print(self.direction(figure.color, figure.form))
        print(button.objectName().__str__())
        icon.addPixmap(QtGui.QPixmap(self.direction(figure.color, figure.form)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button.setIcon(icon)
        button.setIconSize(QtCore.QSize(100, 100))

    def set_icon_to_buttons(self):
        logic_matrix = self.board.get_matrix()
        it = iter(self.but_matrix)
        i = 0
        for i in range(len(logic_matrix)):
            for j in range(len(logic_matrix[0])):
                self.load_icon(logic_matrix[i][j].figure, self.but_matrix[i][j])

    def direction(self, color, form):
        if color == Color.BLUE and form == FigureType.CIRCLE:
            return "../figures/draw-blue-circle.jpg"
        elif color == Color.ORANGE and form == FigureType.CIRCLE:
            return "../figures/draw-orange-circle.jpg"
        elif color == Color.GREEN and form == FigureType.CIRCLE:
            return "../figures/draw-green-circle.jpg"
        elif color == Color.BLUE and form == FigureType.RECTANGLE:
            return "../figures/draw-blue-rectangle.jpg"
        elif color == Color.ORANGE and form == FigureType.RECTANGLE:
            return "../figures/draw-orange-rectangle.jpg"
        elif color == Color.GREEN and form == FigureType.RECTANGLE:
            return "../figures/draw-green-rectangle.jpg"

    def add_buttons(self):

        self.but_matrix[0].append(self.ui.cellButton_1)
        self.but_matrix[0].append(self.ui.cellButton_2)
        self.but_matrix[0].append(self.ui.cellButton_3)
        self.but_matrix[1].append(self.ui.cellButton_4)
        self.but_matrix[1].append(self.ui.cellButton_5)
        self.but_matrix[1].append(self.ui.cellButton_6)
        self.but_matrix[2].append(self.ui.cellButton_7)
        self.but_matrix[2].append(self.ui.cellButton_8)
        self.but_matrix[2].append(self.ui.cellButton_9)

    def get_buttons(self):
        return self.but_matrix
