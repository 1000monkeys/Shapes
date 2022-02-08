from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPainter, QPen, QFont, QFontMetrics, QPainterPath
from PyQt5.QtWidgets import QWidget, QApplication


class TrianglePaintWidget(QWidget):
    def __init__(self, parentLayout):
        super().__init__()
        self.parentLayout = parentLayout
        self.screen = QApplication.primaryScreen()

        self.defaultPen = QPen(Qt.black, 5)
        self.defaultPen.setCapStyle(Qt.RoundCap)

        self.highlightPen = QPen(Qt.red, 12)
        self.highlightPen.setCapStyle(Qt.RoundCap)

        self.font = QFont("times", 12)
        self.font.setBold(True)
        self.fontMetrics = QFontMetrics(self.font)

    def sizeHint(self) -> QSize:
        appWidth = self.parentLayout.menu.frameGeometry().width()
        appHeight = self.parentLayout.menu.frameGeometry().height()

        rightVboxWidth = self.parentLayout.vBoxLayout.sizeHint().width()

        size = QSize(appWidth - rightVboxWidth, appHeight)
        return size

    def resizeEvent(self, event):
        QtWidgets.QWidget.resizeEvent(self, event)
        self.update()

    def paintEvent(self, event):
        showHeight = True
        showWidth = True

        painter = QPainter()
        painter.begin(self)
        painter.setFont(self.font)

        appWidth = self.parentLayout.menu.central.frameGeometry().width()
        appHeight = self.parentLayout.menu.central.frameGeometry().height()

        rightVboxWidth = self.parentLayout.vBoxLayout.sizeHint().width()
        painter.scale(((appWidth - rightVboxWidth - 50) / 250.0), ((appHeight - 25) / 250.0))

        if showHeight:
            self.highlightPen.setStyle(Qt.DashLine)
            painter.setPen(self.highlightPen)
            painter.drawLine(125, 225, 125, 25)
            self.highlightPen.setStyle(Qt.SolidLine)

            painter.setPen(self.defaultPen)
            painter.drawLine(125, 225, 125, 25)

            text = "Height"
            width = self.fontMetrics.width(text)
            height = self.fontMetrics.height()
            path = QPainterPath()
            path.addText(125 - (width / 2), 125 - (height / 2), self.font, text)
            painter.fillPath(path, Qt.white)
            painter.strokePath(path, Qt.black)

        if showWidth:
            painter.setPen(self.highlightPen)
            painter.drawLine(225, 225, 25, 225)
            painter.setPen(self.defaultPen)

            text = "width"
            width = self.fontMetrics.width(text)
            path = QPainterPath()
            path.addText(125 - (width / 2), 215, self.font, text)
            painter.fillPath(path, Qt.white)
            painter.strokePath(path, Qt.black)

        painter.setPen(self.defaultPen)

        painter.drawLine(25, 225, 125, 25)
        painter.drawLine(125, 25, 225, 225)
        painter.drawLine(225, 225, 25, 225)

        painter.end()
