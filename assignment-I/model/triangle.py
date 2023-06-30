from model.shape import Shape
from model.point import Point

from PySide6.QtGui import QPainter
from PySide6.QtCore import QRectF, QPoint

import math


class Triangle(Shape):
    def __init__(self, center: Point, side: float):
        super().__init__(center)
        self._side = side

    # TODO: Task 4 - Implement the scale method

    def draw(self, painter: QPainter) -> None:
        # get point info from calc_points method
        # define Qpoints
        x1, x2, x3, y1, y2, y3 = self.calc_points()
        points = [QPoint(x1, y1), QPoint(x2, y2), QPoint(x3, y3)]

        painter.drawPolygon(points)
        painter.drawText(self._center.x - 2, self._center.y, str(self._id))

    def calc_points(self):
        # define the coordinates of the triangle's points based on center and side length
        beta = 30 * math.pi / 180
        x1 = self._center.x - (2 / 3) * self._side * math.cos(beta)  
        x2 = self._center.x
        x3 = self._center.x + (2 / 3) * self._side * math.cos(beta)  

        y1 = y3 = self._center.y + (1 / 3) * self._side * math.cos(beta)
        y2 = self._center.y - (2 / 3) * self._side * math.cos(beta)

        return x1, x2, x3, y1, y2, y3
