import math

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPainter, QPen, QFont, QFontMetrics, QPainterPath
from PyQt5.QtWidgets import QWidget, QApplication

from shapes.triangle import Triangle


class TrianglePaintWidget(QWidget):
    def __init__(self, parentLayout, triangle):
        __init__(self, parentLayout)
        self.triangle = triangle

    def __init__(self, parentLayout):
        super().__init__()
        self.triangle = None

        self.parentLayout = parentLayout
        self.screen = QApplication.primaryScreen()

        self.defaultPen = QPen(Qt.black, 5)
        self.defaultPen.setCapStyle(Qt.RoundCap)

        self.highlightPen = QPen(Qt.red, 12)
        self.highlightPen.setCapStyle(Qt.RoundCap)

        self.font = QFont("times", 12)
        self.font.setBold(True)
        self.fontMetrics = QFontMetrics(self.font)

    def getSize(self):
        appWidth = self.parentLayout.menu.central.frameGeometry().width()
        appHeight = self.parentLayout.menu.central.frameGeometry().height()

        rightVboxWidth = self.parentLayout.vBoxLayout.sizeHint().width()

        return QSize(appWidth - rightVboxWidth, appHeight)

    def sizeHint(self) -> QSize:
        return self.getSize()

    def resizeEvent(self, event):
        QtWidgets.QWidget.resizeEvent(self, event)
        self.update()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setFont(self.font)

        size = self.getSize()

        painter.scale(float(size.width()) / 250.0, float(size.height()) / 250.0)

        print("1")

        self.triangle = Triangle((5, 4, 3), (90, 45, 45))

        if self.triangle.edges[0] > self.triangle.edges[1] and self.triangle.edges[0] > self.triangle.edges[2]:
            self.scale = 200.0 / self.triangle.edges[0]
        elif self.triangle.edges[1] > self.triangle.edges[0] and self.triangle.edges[1] > self.triangle.edges[2]:
            self.scale = 200.0 / self.triangle.edges[1]
        elif self.triangle.edges[2] > self.triangle.edges[0] and self.triangle.edges[2] > self.triangle.edges[1]:
            self.scale = 200.0 / self.triangle.edges[2]

        self.scale = float(200.0 / self.triangle.edges[0])
        print("2")

        """
        painter.setPen(self.defaultPen)
        xa = float(self.triangle.sideA * math.cos(math.radians(0)) * self.scale)
        ya = float(self.triangle.sideA * math.sin(math.radians(0)) * self.scale)
        print("XA:" + str(25 + xa) + " & YA:" + str(225 - ya))
        painter.drawLine(25 + 5, 225, 25 + xa, 225 - ya)

        angle = 180 - 45  # (135)

        xb = float(self.triangle.sideB * math.cos(math.radians(angle)) * self.scale)
        yb = float(self.triangle.sideB * math.sin(math.radians(angle)) * self.scale)
        print("XB:" + str(25 + xb + xa) + " & YB:" + str(225 - ya - yb))
        painter.drawLine(25 + xa, 225 - ya, 25 + xa + xb, 225 - ya - yb)

        angle = 180 + 45 + 45

        xc = float(self.triangle.sideC * math.cos(math.radians(angle)) * self.scale)
        yc = float(self.triangle.sideC * math.sin(math.radians(angle)) * self.scale)
        print("XC:" + str(25 + xa + xb + xc) + " & YC:" + str(225 - ya - yb - yc))
        painter.drawLine(25 + xa + xb, 225 - ya - yb, 25 + xa + xb + xc, 225 - ya - yb - yc)
        #painter.drawLine(25 + xa + xb, 225 - ya - yb, 25, 225)
        """

        painter.setPen(self.defaultPen)
        angle = 0
        xa = float(self.triangle.edges[1] * math.cos(math.radians(angle))) * self.scale
        ya = float(self.triangle.edges[1] * math.sin(math.radians(angle))) * self.scale
        print("XA:" + str(25 + xa) + " & YA:" + str(25 + ya))
        painter.drawLine(25, 25, 25 + xa, 25 + ya)

        angle = self.triangle.angles[0]
        xb = float(self.triangle.edges[0] * math.cos(math.radians(angle))) * self.scale
        yb = float(self.triangle.edges[0] * math.sin(math.radians(angle))) * self.scale
        print("XB:" + str(25 + xb) + " & YB:" + str(25 + yb))
        painter.drawLine(25 + xa, 25 + ya, 25 + xb, 25 + yb)

        angle = 90 - self.triangle.angles[0] - self.triangle.angles[1] - self.triangle.angles[2]
        xc = float(self.triangle.edges[0] * math.cos(math.radians(angle))) * self.scale
        yc = float(self.triangle.edges[0] * math.sin(math.radians(angle))) * self.scale
        print("XC:" + str(25 + xc) + " & YC:" + str(25 + yc))
        painter.drawLine(25 + xb, 25 + yb, 25 + xc, 25 + yc + yb)



        """
        angle = 0
        xb = float(self.triangle.edges[1] * math.cos(math.radians(angle))) * self.scale
        yb = float(self.triangle.edges[1] * math.sin(math.radians(angle))) * self.scale
        print("XB:" + str(25 + xa + xb) + " & YB:" + str(25 + ya + yb))
        painter.drawLine(25 + xa, 25 + ya, (25 + xa) + xb, (25 + ya) + yb)

        angle = self.triangle.angles[1]
        xc = float(self.triangle.edges[1] * math.cos(math.radians(angle))) * self.scale
        yc = float(self.triangle.edges[1] * math.sin(math.radians(angle))) * self.scale
        print("XC:" + str(25 + xa + xb + xc) + " & YC:" + str(25 + ya + yb + yc))
        painter.drawLine(25 + xa + xb, 25 + ya + yb, 25 + xa + xb - xc, 25 + ya + yb + yc)
        """
    """
    def paintEvent(self, event):
        showHeight = False
        showWidth = False

        painter = QPainter()
        painter.begin(self)
        painter.setFont(self.font)

        size = self.getSize()

        painter.scale(float(size.width()) / 250.0, float(size.height()) / 250.0)

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


        path = QPainterPath()
        text = "A"
        width = self.fontMetrics.width(text)
        path.addText(125 - (width / 2), 220, self.font, text)
        text = "B"
        width = self.fontMetrics.width(text)
        path.addText(85 - (width / 2), 137, self.font, text)
        text = "C"
        width = self.fontMetrics.width(text)
        path.addText(165 - (width / 2), 137, self.font, text)
        text = "1"
        width = self.fontMetrics.width(text)
        path.addText(18 - (width / 2), 232, self.font, text)
        text = "2"
        width = self.fontMetrics.width(text)
        path.addText(125 - (width / 2), 20, self.font, text)
        text = "3"
        width = self.fontMetrics.width(text)
        path.addText(232 - (width / 2), 232, self.font, text)

        painter.fillPath(path, Qt.white)
        painter.strokePath(path, Qt.black)

        painter.end()
        """