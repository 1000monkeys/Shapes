import math

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QGridLayout, QWidget

from shapes.isFloat import isFloat


class EllipseMenu(QWidget):
    def calculate(self):
        self.heightInput.setText(self.heightInput.text().replace(",", "."))

        if isFloat(self.heightInput.text()) and isFloat(self.widthInput.text()):
            width = int(self.widthInput.text())
            height = int(self.heightInput.text())

            oppervlakte = math.pi * width * height

            self.resultLabel.setText("Oppervlakte: " + str(oppervlakte))
        else:
            self.resultLabel.setText("Check input.")

    def getUI(self, menu):
        menu.setWindowTitle("Ellipse Shape")
        menu.setFixedWidth(500)
        menu.setFixedHeight(275)

        ellipsePicture = QLabel(self)
        ellipsePixMap = QPixmap('assets/ellipse.png')
        ellipsePixMap = ellipsePixMap.scaled(250, 250)
        ellipsePicture.setPixmap(ellipsePixMap)
        ellipsePicture.show()

        self.widthLabel = QLabel(self, text="Width: ")
        self.widthInput = QLineEdit(self)
        self.widthInput.textChanged.connect(self.calculate)

        self.heightLabel = QLabel(self, text="Height: ")
        self.heightInput = QLineEdit(self)
        self.heightInput.textChanged.connect(self.calculate)

        self.resultLabel = QLabel(self, text="Check input.")

        self.backButton = QPushButton(self, text="Terug")
        self.backButton.clicked.connect(menu.goToMenu)


        layout = QGridLayout()
        layout.addWidget(ellipsePicture, 0, 0, 4, 4)

        layout.addWidget(self.widthLabel, 0, 4)
        layout.addWidget(self.widthInput, 0, 5)

        layout.addWidget(self.heightLabel, 1, 4)
        layout.addWidget(self.heightInput, 1, 5)

        layout.addWidget(self.resultLabel, 2, 4, 1, 2)
        layout.addWidget(self.backButton, 3, 4, 1, 2)

        return layout