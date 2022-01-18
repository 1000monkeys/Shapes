import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QGridLayout, QWidget


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Shapes By Kjell Vos")

        central = QWidget()
        self.setCentralWidget(central)
        layout = QGridLayout()
        central.setLayout(layout)

        cilinderPixMap = QPixmap('assets/cilinder.png')
        circlePixMap = QPixmap('assets/circle.png')
        cubePixMap = QPixmap('assets/cube.png')
        kitePixMap = QPixmap('assets/kite.png')
        parellogramPixMap = QPixmap('assets/parellogram.png')
        pyramidPixMap = QPixmap('assets/pyramid.png')
        squarePixMap = QPixmap('assets/square.png')
        squareTrianglePixMap = QPixmap('assets/squareTriangle.png')
        trianglePixMap = QPixmap('assets/triangle.png')

        cilinderLabel = QLabel(self)
        cilinderLabel.setPixmap(cilinderPixMap)
        cilinderLabel.mousePressEvent = self.cilinderClick
        cilinderLabel.show()

        circleLabel = QLabel(self)
        circleLabel.setPixmap(circlePixMap)
        circleLabel.mousePressEvent = self.circleClick
        circleLabel.show()

        cubeLabel = QLabel(self)
        cubeLabel.setPixmap(cubePixMap)
        cubeLabel.mousePressEvent = self.cubeClick
        cubeLabel.show()

        kiteLabel = QLabel(self)
        kiteLabel.setPixmap(kitePixMap)
        kiteLabel.mousePressEvent = self.kiteClick
        kiteLabel.show()

        parellogramLabel = QLabel(self)
        parellogramLabel.setPixmap(parellogramPixMap)
        parellogramLabel.mousePressEvent = self.parellogramClick
        parellogramLabel.show()

        pyramidLabel = QLabel(self)
        pyramidLabel.setPixmap(pyramidPixMap)
        pyramidLabel.mousePressEvent = self.pyramidClick
        pyramidLabel.show()

        squareLabel = QLabel(self)
        squareLabel.setPixmap(squarePixMap)
        squareLabel.mousePressEvent = self.squareClick
        squareLabel.show()

        squareTriangleLabel = QLabel(self)
        squareTriangleLabel.setPixmap(squareTrianglePixMap)
        squareTriangleLabel.mousePressEvent = self.squareTriangleClick
        squareTriangleLabel.show()

        triangleLabel = QLabel(self)
        triangleLabel.setPixmap(trianglePixMap)
        triangleLabel.mousePressEvent = self.triangleClick
        triangleLabel.show()

        layout.addWidget(cilinderLabel, 0, 0)
        layout.addWidget(circleLabel, 0, 1)
        layout.addWidget(cubeLabel, 0, 2)
        layout.addWidget(kiteLabel, 0, 3)

        layout.addWidget(parellogramLabel, 1, 0)
        layout.addWidget(pyramidLabel, 1, 1)
        layout.addWidget(squareLabel, 1, 2)
        layout.addWidget(squareTriangleLabel, 1, 3)

        layout.addWidget(triangleLabel, 2, 0)

        self.setLayout(layout)

    def cilinderClick(self, event):
        print("PRESSED")

    def circleClick(self, event):
        print("PRESSED")

    def cubeClick(self, event):
        print("PRESSED")

    def kiteClick(self, event):
        print("PRESSED")

    def parellogramClick(self, event):
        print("PRESSED")

    def pyramidClick(self, event):
        print("PRESSED")

    def squareClick(self, event):
        print("PRESSED")

    def squareTriangleClick(self, event):
        print("PRESSED")

    def triangleClick(self, event):
        print("PRESSED")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec_())
