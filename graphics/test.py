from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, Qt, QRect
from PyQt5.QtGui import QIcon, QPixmap


# Наследуемся от QMainWindow
class MainWindow(QMainWindow):
    # Переопределяем конструктор класса
    def __init__(self):
        # Обязательно нужно вызвать метод супер класса
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(630, 630))  # Устанавливаем размеры
        self.setWindowTitle("Работа с QTableWidget")  # Устанавливаем заголовок окна
        central_widget = QWidget(self)  # Создаём центральный виджет
        self.setCentralWidget(central_widget)  # Устанавливаем центральный виджет

        vertical_layout = QVBoxLayout(central_widget)
        vertical_layout.setGeometry(QRect(20, 20, 100, 100))

        table = QTableWidget(self)  # Создаём таблицу
        table.setColumnCount(3)  # Устанавливаем три колонки
        table.setRowCount(3)  # и одну строку в таблице
        table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        table.horizontalHeader().hide()
        table.verticalHeader().hide()

        table.setItem(0, 0, QTableWidgetItem("Text in column 1"))
        label = QLabel()
        label.setPixmap(QPixmap("../figures/draw-blue-circle.jpg"))
        table.setCellWidget(0, 1, label)

        hor_layout = QHBoxLayout(central_widget)


        self.verticalLayout.addLayout(self.horizontalLayout_1)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.restartButton = QtWidgets.QPushButton(self.centralwidget)
        self.restartButton.setGeometry(QRect(0, 10, 101, 31))
        self.restartButton.setObjectName("restartButton")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QRect(300, 20, 81, 23))
        self.nextButton.setObjectName("nextButton")
        self.prevButton = QtWidgets.QPushButton(self.centralwidget)
        self.prevButton.setGeometry(QRect(220, 20, 81, 23))
        self.prevButton.setObjectName("prevButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QRect(220, 0, 51, 21))
        self.label.setObjectName("label")
        self.levelLabel = QtWidgets.QLabel(self.centralwidget)
        self.levelLabel.setGeometry(QRect(270, 0, 47, 21))
        self.levelLabel.setObjectName("levelLabel")
        self.successMoveLabel = QtWidgets.QLabel(self.centralwidget)
        self.successMoveLabel.setGeometry(QRect(130, 20, 91, 20))
        self.successMoveLabel.setText("")
        self.successMoveLabel.setObjectName("successMoveLabel")

        label1 = QLabel("10100")
        vertical_layout.addWidget(label1)
        vertical_layout.addWidget(table)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
