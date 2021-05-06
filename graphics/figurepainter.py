from PIL import Image, ImageDraw
from logic.logic import Color, FigureType, Figure


def create_figures():
    color = "gray"
    im = Image.new('RGB', (100, 100), color)
    c = Circle(50, 50, 50)
    c.draw(im, 'orange')
    im.save('figures/draw-orange-circle.jpg', quality=95)

    im = Image.new('RGB', (100, 100), color)
    c.draw(im, 'blue')
    im.save('figures/draw-blue-circle.jpg', quality=95)

    im = Image.new('RGB', (100, 100), color)
    c.draw(im, 'green')
    im.save('figures/draw-green-circle.jpg', quality=95)

    im = Image.new('RGB', (100, 100), color)
    r = Rectangle(10, 10, 80, 80)
    r.draw(im, "orange")

    im.save('figures/draw-orange-rectangle.jpg', quality=95)

    im = Image.new('RGB', (100, 100), color)
    r.draw(im, "blue")
    im.save('figures/draw-blue-rectangle.jpg', quality=95)

    im = Image.new('RGB', (100, 100), color)
    r.draw(im, "green")
    im.save('figures/draw-green-rectangle.jpg', quality=95)


class Circle:
    def __init__(self, x0, y0, r):
        self.__x0 = x0
        self.__y0 = y0
        if r < 0:
            raise ValueError("Ввели отрицательный радиус")
        elif r == 0:
            raise ValueError("Полученная окружность является точкой, r=0")
        else:
            self.__r = r

    def draw(self, im: Image, color: str):
        draw = ImageDraw.Draw(im)
        x = self.__x0
        y = self.__y0
        r = self.__r
        draw.ellipse(
            xy=(x - r, y - r,
                x + r, y + r),
            fill=color,
            outline=color,
            width=4
        )


class Rectangle:
    def __init__(self, x, y, w, h):
        self.h = h
        self.w = w
        self.x = x
        self.y = y

    def draw(self, im: Image, color: str):
        draw = ImageDraw.Draw(im)
        draw.rectangle(xy=(self.x, self.y,
                           self.x + self.w, self.h + self.y),
                       fill=color,
                       outline=color,
                       width=4)


class FigurePainter:

    def draw_figure(self, figure: Figure):
        im = Image.new('RGB', (100, 100), figure.color)
        if figure.form == FigureType.CIRCLE:
            circle = Circle(50, 50, 45)
            circle.draw(im, figure.color)
        elif figure.form == FigureType.RECTANGLE:
            rec = Rectangle(10, 10, 80, 80)
            rec.draw(im, figure.color)
        else:
            raise ValueError('Painter Figure Type error')

        self.create_flag(im)
        # im.toqpixmap()
        im.save('figures/draw-' + color.value + '-' + f_type.value + '.jpg', quality=95)

    def create_flag(self, im, x=30, y=10):
        draw = ImageDraw.Draw(im)
        draw.polygon(
            xy=((x, y), (x + 5, y), (x + 5, y + 5), (x + 20, y + 20), (x + 5, y + 35), (x + 5, y + 70), (x, y + 70)),
            fill="red", outline="black")
