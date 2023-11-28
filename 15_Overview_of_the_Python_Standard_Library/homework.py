# Возьмите любые 1-3 задачи из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из командной строки с передачей параметров.

import logging
import argparse


class Rectangle:
    def __init__(self, width, height=None):
        if width <= 0 or height <= 0:
            logger.error(f'Стороны должны быть положительными')
        else:
            self.width = width
            if height is None:
                self.height = width
            else:
                self.height = height

    def perimeter(self):
        perimeter = 2 * (self.width + self.height)
        logger.info(f'"{self}" имеет периметр {perimeter}')
        return perimeter

    def area(self):
        area = self.width * self.height
        logger.info(f'"{self}" имеет площадь {area}')
        return area

    def __str__(self):
        return f'Прямоугольник {self.width} х {self.height}'

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    def __add__(self, other):
        p = self.perimeter() + other.perimeter()
        width = self.width + other.width
        height = int(p / 2 - width)
        logger.info(f'Сумма объектов "{self}" и "{other}": объект "{Rectangle(width, height)}"')
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() > other.perimeter():
            p = self.perimeter() - other.perimeter()
            width = abs(self.width - other.width)
            height = int(p / 2 - width)
            logger.info(f'Разность объектов "{self}" и "{other}": объект "{Rectangle(width, height)}"')
            return Rectangle(width, height)
        else:
            logger.error(f'{self} меньше, чем {other}')

    def __eq__(self, other):
        logger.info(f'"{self}" и "{other}" имеют равные площади: {self.area() == other.area()}')
        return self.area() == other.area()

    def __lt__(self, other):
        logger.info(f'"{self}" имеет площадь меньшую, чем "{other}": {self.area() < other.area()}')
        return self.area() < other.area()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Working with rectangles')
    parser.add_argument('-a1', metavar='a1', type=int, help='enter the width of the first rectangle')
    parser.add_argument('-b1', metavar='b1', type=int, help='enter the height of the first rectangle')
    parser.add_argument('-a2', metavar='a2', type=int, help='enter the width of the second rectangle')
    parser.add_argument('-b2', metavar='b2', type=int, help='enter the height of the second rectangle')
    args = parser.parse_args()

    FORMAT = '{levelname:<5} - {asctime}. Method: {funcName}. Result: {msg}'
    logging.basicConfig(format=FORMAT, style='{', filename='./15_Overview_of_the_Python_Standard_Library/hw.log', encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger(__name__)

    rect1 = Rectangle(args.a1, args.b1)
    rect2 = Rectangle(args.a2, args.b2)

    rect1.perimeter()
    rect2.perimeter()
    rect1.area()
    rect2.area()
    rect1 + rect2
    rect1 - rect2
    rect1 == rect2
    rect1 < rect2
