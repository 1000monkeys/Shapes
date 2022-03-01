import math

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QGridLayout, QWidget

from menus.stringFormat import isFloat


class ConeMenu(QWidget):
    def calculate(self):
        self.heightInput.setText(self.heightInput.text().replace(",", "."))
        self.radiusInput.setText(self.radiusInput.text().replace(",", "."))

        if isFloat(self.heightInput.text()) and isFloat(self.radiusInput.text()):
            height = float(self.heightInput.text())
            radius = float(self.radiusInput.text())

            oppervlakte = math.pi * (radius * radius)
            oppervlakte = oppervlakte + (math.pi * radius * math.sqrt((height * height) + (radius * radius)))

            volume = (1/3) * math.pi * (radius * radius)

            self.resultLabel.setText("Oppervlakte: " + str(oppervlakte) + "\nInhoud: " + str(volume))
        else:
            self.resultLabel.setText("Check input.")

    def getUI(self, menu):
        menu.setWindowTitle("Cone Shape")
        menu.setFixedWidth(500)
        menu.setFixedHeight(275)

        conePicture = QLabel(self)
        conePixMap = QPixmap('assets/cone.png')
        conePixMap = conePixMap.scaled(250, 250)
        conePicture.setPixmap(conePixMap)
        conePicture.show()

        #radius and height
        self.radiusLabel = QLabel(self, text="Radius: ")
        self.radiusInput = QLineEdit(self)
        self.radiusInput.textChanged.connect(self.calculate)

        self.heightLabel = QLabel(self, text="Height: ")
        self.heightInput = QLineEdit(self)
        self.heightInput.textChanged.connect(self.calculate)


        self.resultLabel = QLabel(self, text="Check input.")

        self.backButton = QPushButton(self, text="Terug")
        self.backButton.clicked.connect(menu.goToMenu)


        layout = QGridLayout()
        layout.addWidget(conePicture, 0, 0, 4, 4)

        layout.addWidget(self.radiusLabel, 0, 4)
        layout.addWidget(self.radiusInput, 0, 5)

        layout.addWidget(self.heightLabel, 1, 4)
        layout.addWidget(self.heightInput, 1, 5)

        layout.addWidget(self.resultLabel, 2, 4, 1, 2)
        layout.addWidget(self.backButton, 3, 4, 1, 2)

        return layout