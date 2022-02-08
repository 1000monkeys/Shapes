from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QWidget


class PaintWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.defaultPen = QPen(Qt.black, 5)
        self.highlightPen = QPen(Qt.red, 5)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(QPen(Qt.black, 5))
        painter.end()
