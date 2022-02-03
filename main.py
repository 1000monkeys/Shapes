import os
import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QPushButton, QLabel, QVBoxLayout

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

        #self.setFixedWidth(600)
        #self.setFixedHeight(600)

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
        """Square"""
        # Button
        squareButton = QPushButton()
        squareButton.clicked.connect(self.squareClick)
        squareButton.setIcon(QIcon('assets/square.png'))
        squareButton.setIconSize(QSize(100, 100))
        # squareButton.setFixedSize(QSize(105, 105))
        # Label
        squareLabel = QLabel("Square")
        squareLabel.setAlignment(Qt.AlignCenter)
        # VBox
        squareVBox = QVBoxLayout()
        squareVBox.addWidget(squareButton)
        squareVBox.addWidget(squareLabel)

        """Circle"""
        # Button
        circleButton = QPushButton()
        circleButton.clicked.connect(self.circleClick)
        circleButton.setIcon(QIcon('assets/circle.png'))
        circleButton.setIconSize(QSize(100, 100))
        # Label
        circleLabel = QLabel("Circle")
        circleLabel.setAlignment(Qt.AlignCenter)
        # VBox
        circleVBox = QVBoxLayout()
        circleVBox.addWidget(circleButton)
        circleVBox.addWidget(circleLabel)

        """Triangle"""
        # Button
        triangleButton = QPushButton()
        triangleButton.clicked.connect(self.triangleClick)
        triangleButton.setIcon(QIcon('assets/triangle.png'))
        triangleButton.setIconSize(QSize(100, 100))
        # Label
        triangleLabel = QLabel("Triangle")
        triangleLabel.setAlignment(Qt.AlignCenter)
        # VBox
        triangleVBox = QVBoxLayout()
        triangleVBox.addWidget(triangleButton)
        triangleVBox.addWidget(triangleLabel)

        """Pythagorean Triangle"""
        # Button
        squareTriangleButton = QPushButton()
        squareTriangleButton.clicked.connect(self.squareTriangleClick)
        squareTriangleButton.setIcon(QIcon('assets/squareTriangle.png'))
        squareTriangleButton.setIconSize(QSize(100, 100))
        # Label
        squareTriangleLabel = QLabel("Pythagorean triangle")
        squareTriangleLabel.setAlignment(Qt.AlignCenter)
        # VBox
        squareTriangleVBox = QVBoxLayout()
        squareTriangleVBox.addWidget(squareTriangleButton)
        squareTriangleVBox.addWidget(squareTriangleLabel)

        """Kite"""
        # Button
        kiteButton = QPushButton()
        kiteButton.clicked.connect(self.kiteClick)
        kiteButton.setIcon(QIcon('assets/kite.png'))
        kiteButton.setIconSize(QSize(100, 100))
        # Label
        kiteLabel = QLabel("Kite")
        kiteLabel.setAlignment(Qt.AlignCenter)
        # VBox
        kiteVBox = QVBoxLayout()
        kiteVBox.addWidget(kiteButton)
        kiteVBox.addWidget(kiteLabel)

        """Cube"""
        # Button
        cubeButton = QPushButton()
        cubeButton.clicked.connect(self.cubeClick)
        cubeButton.setIcon(QIcon('assets/cube.png'))
        cubeButton.setIconSize(QSize(100, 100))
        # Label
        cubeLabel = QLabel("Cube")
        cubeLabel.setAlignment(Qt.AlignCenter)
        # VBox
        cubeVBox = QVBoxLayout()
        cubeVBox.addWidget(cubeButton)
        cubeVBox.addWidget(cubeLabel)

        """Cilinder"""
        # Button
        cilinderButton = QPushButton()
        cilinderButton.clicked.connect(self.cilinderClick)
        cilinderButton.setIcon(QIcon('assets/cilinder.png'))
        cilinderButton.setIconSize(QSize(100, 100))
        # Label
        cilinderLabel = QLabel("Cilinder")
        cilinderLabel.setAlignment(Qt.AlignCenter)
        # VBox
        cilinderVBox = QVBoxLayout()
        cilinderVBox.addWidget(cilinderButton)
        cilinderVBox.addWidget(cilinderLabel)

        """Pyramid"""
        # Button
        pyramidButton = QPushButton()
        pyramidButton.clicked.connect(self.pyramidClick)
        pyramidButton.setIcon(QIcon('assets/pyramid.png'))
        pyramidButton.setIconSize(QSize(100, 100))
        # Label
        pyramidLabel = QLabel("Pyramid")
        pyramidLabel.setAlignment(Qt.AlignCenter)
        # VBox
        pyramidVBox = QVBoxLayout()
        pyramidVBox.addWidget(pyramidButton)
        pyramidVBox.addWidget(pyramidLabel)

        """Parellogram"""
        # Button
        parellogramButton = QPushButton()
        parellogramButton.clicked.connect(self.parellogramClick)
        parellogramButton.setIcon(QIcon('assets/parellogram.png'))
        parellogramButton.setIconSize(QSize(100, 100))
        # Label
        parellogramLabel = QLabel("Parellogram")
        parellogramLabel.setAlignment(Qt.AlignCenter)
        # VBox
        parellogramVBox = QVBoxLayout()
        parellogramVBox.addWidget(parellogramButton)
        parellogramVBox.addWidget(parellogramLabel)

        """Trapezium"""
        # Button
        trapeziumButton = QPushButton()
        trapeziumButton.clicked.connect(self.trapeziumClick)
        trapeziumButton.setIcon(QIcon('assets/trapezium.png'))
        trapeziumButton.setIconSize(QSize(100, 100))
        # Label
        trapeziumLabel = QLabel("Trapezium")
        trapeziumLabel.setAlignment(Qt.AlignCenter)
        # VBox
        trapeziumVBox = QVBoxLayout()
        trapeziumVBox.addWidget(trapeziumButton)
        trapeziumVBox.addWidget(trapeziumLabel)

        """Prisma Triangle"""
        # Button
        prismaTriangleButton = QPushButton()
        prismaTriangleButton.clicked.connect(self.prismaTriangleClick)
        prismaTriangleButton.setIcon(QIcon('assets/prismaTriangle.png'))
        prismaTriangleButton.setIconSize(QSize(100, 100))
        # Label
        prismaTriangleLabel = QLabel("Prisma Triangle")
        prismaTriangleLabel.setAlignment(Qt.AlignCenter)
        # VBox
        prismaTriangleVBox = QVBoxLayout()
        prismaTriangleVBox.addWidget(prismaTriangleButton)
        prismaTriangleVBox.addWidget(prismaTriangleLabel)

        """Cone"""
        # Button
        coneButton = QPushButton()
        coneButton.clicked.connect(self.coneClick)
        coneButton.setIcon(QIcon('assets/cone.png'))
        coneButton.setIconSize(QSize(100, 100))
        # Label
        coneLabel = QLabel("Cone")
        coneLabel.setAlignment(Qt.AlignCenter)
        # VBox
        coneVBox = QVBoxLayout()
        coneVBox.addWidget(coneButton)
        coneVBox.addWidget(coneLabel)

        """Sphere"""
        # Sphere
        sphereButton = QPushButton()
        sphereButton.clicked.connect(self.sphereClick)
        sphereButton.setIcon(QIcon('assets/sphere.png'))
        sphereButton.setIconSize(QSize(100, 100))
        # Label
        sphereLabel = QLabel("Sphere")
        sphereLabel.setAlignment(Qt.AlignCenter)
        # VBox
        sphereVBox = QVBoxLayout()
        sphereVBox.addWidget(sphereButton)
        sphereVBox.addWidget(sphereLabel)

        """Ellipse"""
        # Button
        ellipseButton = QPushButton()
        ellipseButton.clicked.connect(self.ellipseClick)
        ellipseButton.setIcon(QIcon('assets/ellipse.png'))
        ellipseButton.setIconSize(QSize(100, 100))
        # Label
        ellipseLabel = QLabel("Ellipse")
        ellipseLabel.setAlignment(Qt.AlignCenter)
        # VBox
        ellipseVBox = QVBoxLayout()
        ellipseVBox.addWidget(ellipseButton)
        ellipseVBox.addWidget(ellipseLabel)

        """Main layout containing all shapes their buttons and labels inside their resprective VBoxLayout"""
        layout = QGridLayout()
        layout.setHorizontalSpacing(10)
        layout.setVerticalSpacing(15)

        layout.addLayout(squareVBox, 0, 0)
        layout.addLayout(circleVBox, 0, 1)
        layout.addLayout(triangleVBox, 0, 2)
        layout.addLayout(squareTriangleVBox, 0, 3)

        layout.addLayout(kiteVBox, 1, 0)
        layout.addLayout(cubeVBox, 1, 1)
        layout.addLayout(cilinderVBox, 1, 2)
        layout.addLayout(pyramidVBox, 1, 3)

        layout.addLayout(parellogramVBox, 2, 0)
        layout.addLayout(trapeziumVBox, 2, 1)
        layout.addLayout(prismaTriangleVBox, 2, 2)
        layout.addLayout(coneVBox, 2, 3)

        layout.addLayout(sphereVBox, 3, 1)
        layout.addLayout(ellipseVBox, 3, 2)

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
