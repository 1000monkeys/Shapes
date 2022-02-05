from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget


class PaintWidget(QWidget):
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        qp.end()
