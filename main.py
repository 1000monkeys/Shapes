import os
import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QPushButton

from shapes.cilinderShape import CilinderMenu
from shapes.circleShape import CircleMenu
from shapes.coneShape import ConeMenu
from shapes.cubeShape import CubeMenu
from shapes.ellipseShape import EllipseMenu
from shapes.kiteShape import KiteMenu
from shapes.parellogramShape import ParellogramMenu
from shapes.prismaTriangleShape import PrismaTriangleMenu
from shapes.pyramidShape import PyramidMenu
from shapes.sphereShape import SphereMenu
from shapes.squareShape import SquareMenu
from shapes.squareTriangleShape import SquareTriangleMenu
from shapes.trapeziumShape import TrapeziumMenu
from shapes.triangleShape import TriangleMenu


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shapes By Kjell Vos")

        self.setFixedWidth(600)
        self.setFixedHeight(600)

        self.central = QWidget()
        self.setCentralWidget(self.central)
        self.layout = self.mainMenuUI()
        self.central.setLayout(self.layout)

    def goToMenu(self):
        self.setWindowTitle("Shapes By Kjell Vos")

        self.setFixedWidth(600)
        self.setFixedHeight(600)

        deleteItemsOfLayout(self.layout)
        self.central = QWidget()
        self.setCentralWidget(self.central)
        self.layout = self.mainMenuUI()
        self.central.setLayout(self.layout)

    def mainMenuUI(self):
        squareButton = QPushButton()
        squareButton.clicked.connect(self.squareClick)
        squareButton.setIcon(QIcon('assets/square.png'))
        squareButton.setIconSize(QSize(100, 100))

        circleButton = QPushButton()
        circleButton.clicked.connect(self.circleClick)
        circleButton.setIcon(QIcon('assets/circle.png'))
        circleButton.setIconSize(QSize(100, 100))

        triangleButton = QPushButton()
        triangleButton.clicked.connect(self.triangleClick)
        triangleButton.setIcon(QIcon('assets/triangle.png'))
        triangleButton.setIconSize(QSize(100, 100))

        squareTriangleButton = QPushButton()
        squareTriangleButton.clicked.connect(self.squareTriangleClick)
        squareTriangleButton.setIcon(QIcon('assets/squareTriangle.png'))
        squareTriangleButton.setIconSize(QSize(100, 100))

        kiteButton = QPushButton()
        kiteButton.clicked.connect(self.kiteClick)
        kiteButton.setIcon(QIcon('assets/kite.png'))
        kiteButton.setIconSize(QSize(100, 100))

        cubeButton = QPushButton()
        cubeButton.clicked.connect(self.cubeClick)
        cubeButton.setIcon(QIcon('assets/cube.png'))
        cubeButton.setIconSize(QSize(100, 100))

        cilinderButton = QPushButton()
        cilinderButton.clicked.connect(self.cilinderClick)
        cilinderButton.setIcon(QIcon('assets/cilinder.png'))
        cilinderButton.setIconSize(QSize(100, 100))

        pyramidButton = QPushButton()
        pyramidButton.clicked.connect(self.pyramidClick)
        pyramidButton.setIcon(QIcon('assets/pyramid.png'))
        pyramidButton.setIconSize(QSize(100, 100))

        parellogramButton = QPushButton()
        parellogramButton.clicked.connect(self.parellogramClick)
        parellogramButton.setIcon(QIcon('assets/parellogram.png'))
        parellogramButton.setIconSize(QSize(100, 100))

        trapeziumButton = QPushButton()
        trapeziumButton.clicked.connect(self.trapeziumClick)
        trapeziumButton.setIcon(QIcon('assets/trapezium.png'))
        trapeziumButton.setIconSize(QSize(100, 100))

        prismaTriangleButton = QPushButton()
        prismaTriangleButton.clicked.connect(self.prismaTriangleClick)
        prismaTriangleButton.setIcon(QIcon('assets/prismaTriangle.png'))
        prismaTriangleButton.setIconSize(QSize(100, 100))

        coneButton = QPushButton()
        coneButton.clicked.connect(self.coneClick)
        coneButton.setIcon(QIcon('assets/cone.png'))
        coneButton.setIconSize(QSize(100, 100))

        sphereButton = QPushButton()
        sphereButton.clicked.connect(self.sphereClick)
        sphereButton.setIcon(QIcon('assets/sphere.png'))
        sphereButton.setIconSize(QSize(100, 100))

        ellipseButton = QPushButton()
        ellipseButton.clicked.connect(self.ellipseClick)
        ellipseButton.setIcon(QIcon('assets/ellipse.png'))
        ellipseButton.setIconSize(QSize(100, 100))

        layout = QGridLayout()
        layout.setVerticalSpacing(40)

        layout.addWidget(squareButton, 0, 0)
        layout.addWidget(circleButton, 0, 1)
        layout.addWidget(triangleButton, 0, 2)
        layout.addWidget(squareTriangleButton, 0, 3)

        layout.addWidget(kiteButton, 1, 0)
        layout.addWidget(cubeButton, 1, 1)
        layout.addWidget(cilinderButton, 1, 2)
        layout.addWidget(pyramidButton, 1, 3)

        layout.addWidget(parellogramButton, 2, 0)
        layout.addWidget(trapeziumButton, 2, 1)
        layout.addWidget(prismaTriangleButton, 2, 2)
        layout.addWidget(coneButton, 2, 3)

        layout.addWidget(sphereButton, 3, 1)
        layout.addWidget(ellipseButton, 3, 2)

        return layout

    def changeScreenToShapeMenu(self, shapeMenu):
        deleteItemsOfLayout(self.layout)
        self.central = QWidget()
        self.setCentralWidget(self.central)
        self.shapeMenu = shapeMenu
        self.layout = self.shapeMenu.getUI(self)
        self.central.setLayout(self.layout)

    def squareClick(self, event):
        self.changeScreenToShapeMenu(shapeMenu=SquareMenu())

    def circleClick(self, event):
        self.changeScreenToShapeMenu(shapeMenu=CircleMenu())

    def triangleClick(self, event):
        self.changeScreenToShapeMenu(shapeMenu=TriangleMenu())

    def squareTriangleClick(self, event):
        self.changeScreenToShapeMenu(shapeMenu=SquareTriangleMenu())

    def kiteClick(self, event):
        self.changeScreenToShapeMenu(shapeMenu=KiteMenu())

    def cubeClick(self, event):
        self.changeScreenToShapeMenu(shapeMenu=CubeMenu())

    def cilinderClick(self, event):
        self.changeScreenToShapeMenu(shapeMenu=CilinderMenu())

    def pyramidClick(self, event):
        self.changeScreenToShapeMenu(shapeMenu=PyramidMenu())

    def parellogramClick(self, event):
        self.changeScreenToShapeMenu(shapeMenu=ParellogramMenu())

    def trapeziumClick(self, event):
        self.changeScreenToShapeMenu(shapeMenu=TrapeziumMenu())

    def prismaTriangleClick(self, event):
        self.changeScreenToShapeMenu(shapeMenu=PrismaTriangleMenu())

    def coneClick(self, event):
        self.changeScreenToShapeMenu(shapeMenu=ConeMenu())

    def sphereClick(self, event):
        self.changeScreenToShapeMenu(shapeMenu=SphereMenu())

    def ellipseClick(self, event):
        self.changeScreenToShapeMenu(shapeMenu=EllipseMenu())


def deleteItemsOfLayout(layout):
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
            else:
                deleteItemsOfLayout(item.layout())


if __name__ == '__main__':
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "2"
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec_())
