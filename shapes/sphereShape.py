import math

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QGridLayout, QWidget

from shapes.isFloat import isFloat


class SphereMenu(QWidget):
    def calculate(self):
        self.sizeInput.setText(self.sizeInput.text().replace(",", "."))

        if isFloat(self.sizeInput.text()):
            radius = float(self.sizeInput.text())

            inhoud = (1 + 1/3) * math.pi * (radius * radius * radius)
            oppervlakte = 4 * math.pi * (radius * radius * radius)

            self.resultLabel.setText("Oppervlakte: " + str(oppervlakte) + "\nInhoud: " + str(inhoud))
        else:
            self.resultLabel.setText("Check input.")

    def getUI(self, menu):
        menu.setWindowTitle("Circle Shape")
        menu.setFixedWidth(500)
        menu.setFixedHeight(275)

        spherePicture = QLabel(self)
        spherePixMap = QPixmap('assets/sphere.png')
        spherePixMap = spherePixMap.scaled(250, 250)
        spherePicture.setPixmap(spherePixMap)
        spherePicture.show()

        self.sizeLabel = QLabel(self, text="Radius: ")
        self.sizeInput = QLineEdit(self)
        self.sizeInput.textChanged.connect(self.calculate)

        self.resultLabel = QLabel(self, text="Check input.")

        self.backButton = QPushButton(self, text="Terug")
        self.backButton.clicked.connect(menu.goToMenu)


        layout = QGridLayout()
        layout.addWidget(spherePicture, 0, 0, 3, 3)

        layout.addWidget(self.sizeLabel, 0, 3)
        layout.addWidget(self.sizeInput, 0, 4)
        layout.addWidget(self.resultLabel, 1, 3, 1, 3)
        layout.addWidget(self.backButton, 2, 3, 1, 3)

        return layout