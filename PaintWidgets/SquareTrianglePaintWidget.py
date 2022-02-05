from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QWidget


class SquareTrianglePaintWidget(QWidget):
    def paintEvent(self, event):
        painter = QPainter()

        painter.begin(self)
        painter.setPen(QPen(Qt.black, 5))

        painter.drawText(10, 60, "A")
        painter.drawText(35, 100, "B")
        painter.drawText(45, 65, "C")

        painter.drawLine(5, 5, 5, 105)
        painter.drawLine(5, 105, 105, 105)
        painter.drawLine(105, 105, 5, 5)

        painter.end()
