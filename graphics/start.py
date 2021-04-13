import sys

from PyQt5 import QtWidgets

from graphics.board import GrBoard
from graphics.installer_interface import Ui_MainWindow
from logic.game import Level


def display(s):
    app = QtWidgets.QApplication(s.argv)
    gr = GrBoard(Level(1))
    gr.show()
    s.exit(app.exec_())


if __name__ == "__main__":
    display(sys)