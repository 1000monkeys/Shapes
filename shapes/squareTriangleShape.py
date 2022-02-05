import math

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QGridLayout, QWidget

from PaintWidgets.SquareTrianglePaintWidget import SquareTrianglePaintWidget
from templatePaintWidget import PaintWidget
from shapes.isFloat import isFloat


class SquareTriangleMenu(QWidget):
    def edit(self):
        self.aInput.setText(self.aInput.text().replace(",", "."))
        if isFloat(self.aInput.text()):
            self.aInput.setText(str(float(self.aInput.text())))

        self.bInput.setText(self.bInput.text().replace(",", "."))
        if isFloat(self.bInput.text()):
            self.bInput.setText(str(float(self.bInput.text())))

        self.cInput.setText(self.cInput.text().replace(",", "."))
        if isFloat(self.cInput.text()):
            self.cInput.setText(str(float(self.cInput.text())))

    def calculate(self):
        if len(self.aInput.text()) > 0 and len(self.bInput.text()) > 0 and len(self.cInput.text()) > 0:
            self.resultLabel.setText("A, B and C are filled in, please leave one empty.")
        else:
            if isFloat(self.aInput.text()) and isFloat(self.bInput.text()):
                a = float(self.aInput.text())
                b = float(self.bInput.text())
                c = math.sqrt((a * a) + (b * b))

                self.cInput.setText(str(c))
                self.resultLabel.setText("C was calculated, check it's input.")
            elif isFloat(self.bInput.text()) and isFloat(self.cInput.text()):
                b = float(self.bInput.text())
                c = float(self.cInput.text())
                if b > c or b == c:
                    self.resultLabel.setText("B cannot be larger than or equal to C.")
                else:
                    a = math.sqrt((c * c) - (b * b))

                    self.aInput.setText(str(a))
                    self.resultLabel.setText("A was calculated, check it's input.")
            elif isFloat(self.cInput.text()) and isFloat(self.aInput.text()):
                c = float(self.cInput.text())
                a = float(self.aInput.text())
                if a > c or a == c:
                    self.resultLabel.setText("A cannot be larger than or equal to C.")
                else:
                    b = math.sqrt((c * c) - (a * a))

                    self.bInput.setText(str(b))
                    self.resultLabel.setText("B was calculated, check it's input.")
            else:
                self.resultLabel.setText("Check input.")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(Qt.black)

        print("CALLED")

        painter.drawLine(0, 0, 1000, 1000)
        painter.drawLine(100, 100, 0, 0)
        painter.end(self)

    def getUI(self, menu):
        menu.setWindowTitle("Square Triangle Shape")
        menu.setFixedWidth(500)
        menu.setFixedHeight(275)

        menu.show()
        """
        squareTrianglePicture = QLabel(self)
        squareTrianglePixMap = QPixmap('assets/squareTriangle.png')
        squareTrianglePixMap = squareTrianglePixMap.scaled(215, 215)
        squareTrianglePicture.setPixmap(squareTrianglePixMap)
        squareTrianglePicture.show()

        self.aLabel = QLabel(self, text="A: ")
        self.aInput = QLineEdit(self)
        self.aInput.textChanged.connect(self.edit)

        self.bLabel = QLabel(self, text="B: ")
        self.bInput = QLineEdit(self)
        self.bInput.textChanged.connect(self.edit)

        self.cLabel = QLabel(self, text="C: ")
        self.cInput = QLineEdit(self)
        self.cInput.textChanged.connect(self.edit)

        self.calculateButton = QPushButton("Calculate empty field.")
        self.calculateButton.clicked.connect(self.calculate)

        self.resultLabel = QLabel(self, text="Check input.")

        self.backButton = QPushButton(self, text="Terug")
        self.backButton.clicked.connect(menu.goToMenu)

        layout = QGridLayout()
        layout.addWidget(squareTrianglePicture, 0, 0, 5, 5)

        layout.addWidget(self.aLabel, 0, 5)
        layout.addWidget(self.aInput, 0, 6)
        layout.addWidget(self.bLabel, 1, 5)
        layout.addWidget(self.bInput, 1, 6)
        layout.addWidget(self.cLabel, 2, 5)
        layout.addWidget(self.cInput, 2, 6)

        layout.addWidget(self.resultLabel, 3, 5, 1, 2)
        layout.addWidget(self.calculateButton, 4, 5, 1, 2)
        layout.addWidget(self.backButton, 5, 5, 1, 2)
        return layout
        """
        layout = QGridLayout()
        layout.addWidget(SquareTrianglePaintWidget())

        return layout