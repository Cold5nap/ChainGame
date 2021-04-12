from enum import Enum


class Color(Enum):
    ORANGE = 1
    BLUE = 2
    GREEN = 3


class FigureType(Enum):
    RECTANGLE = 1
    CIRCLE = 2


class Flag(Enum):
    NOT_VISITED = 1
    VISITED = 2


class Cell:
    def __init__(self, figure):
        self.fig = figure
        self.flag = Flag.NOT_VISITED

    @property
    def figure(self):
        return self.fig

    @property
    def flag(self):
        return self.flag

    @figure.setter
    def figure(self, figure):
        self.fig = figure

    @flag.setter
    def flag(self, flag: Flag):
        self._flag = flag


class Figure:
    def __init__(self, color: Color, form: FigureType):
        self.type = form
        self.col = color

    @property
    def form(self):
        return self.type

    @property
    def color(self):
        return self.col

    @form.setter
    def form(self, form):
        self.type = form

    @color.setter
    def color(self, color):
        self.col = color


# table
class LogicMatrix:

    def __init__(self, level):
        self.matrix = [[], [], []]
        if level == 1:
            self.set_level_1()
        """if level == 1 :
            self.set_level_2()"""

    def get_matrix(self):
        return self.matrix.copy()

    def set_level_1(self):
        self.matrix[0].append(Cell(Figure(Color.GREEN, FigureType.RECTANGLE)))
        self.matrix[0].append(Cell(Figure(Color.BLUE, FigureType.RECTANGLE)))
        self.matrix[0].append(Cell(Figure(Color.GREEN, FigureType.CIRCLE)))
        self.matrix[1].append(Cell(Figure(Color.ORANGE, FigureType.CIRCLE)))
        self.matrix[1].append(Cell(Figure(Color.ORANGE, FigureType.RECTANGLE)))
        self.matrix[1].append(Cell(Figure(Color.ORANGE, FigureType.CIRCLE)))
        self.matrix[2].append(Cell(Figure(Color.ORANGE, FigureType.RECTANGLE)))
        self.matrix[2].append(Cell(Figure(Color.BLUE, FigureType.CIRCLE)))
        self.matrix[2].append(Cell(Figure(Color.GREEN, FigureType.CIRCLE)))

    # def make_move(self,x,y):

    # проверка окончена ли игра
    def is_over(self):
        for row in self.matrix:
            for cell in row:
                if cell.flag != Flag.VISITED:
                    return False
        return True
