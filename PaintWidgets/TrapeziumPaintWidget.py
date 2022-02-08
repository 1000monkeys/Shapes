from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QWidget


class TrapeziumPaintWidget(QWidget):
    def paintEvent(self, event):
        painter = QPainter()

        painter.begin(self)
        painter.setPen(QPen(Qt.black, 5))

        painter.drawText(80, 15, "Upside")
        painter.drawText(170, 70, "Height")
        painter.drawText(80, 140, "Bottom")

        painter.drawLine(50, 25, 25, 125)
        painter.drawLine(25, 125, 175, 125)
        painter.drawLine(175, 125, 150, 25)
        painter.drawLine(150, 25, 50, 25)

        painter.end()
