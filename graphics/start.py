import sys

from PyQt5 import QtWidgets

from graphics.board import GrBoard
from graphics.installer_interface import Ui_MainWindow
from logic.game import LogicMatrix


def display(s):
    app = QtWidgets.QApplication(s.argv)
    gr = GrBoard(LogicMatrix(1))
    gr.show()
    s.exit(app.exec_())


if __name__ == "__main__":
    display(sys)
"""  app = QtWidgets.QApplication(sys.argv)
  MainWindow = QtWidgets.QMainWindow()
  ui = Ui_MainWindow()
  ui.setupUi(MainWindow)
  MainWindow.show()
  sys.exit(app.exec_())"""