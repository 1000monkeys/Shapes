import math

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QGridLayout, QWidget

from shapes.isFloat import isFloat


class CilinderMenu(QWidget):
    def calculate(self):
        self.heightInput.setText(self.heightInput.text().replace(",", "."))
        self.radiusInput.setText(self.radiusInput.text().replace(",", "."))

        if isFloat(self.heightInput.text()) and isFloat(self.radiusInput.text()):
            height = float(self.heightInput.text())
            radius = float(self.radiusInput.text())

            self.resultLabel.setText("Inhoud: " + str(radius * math.pi * height))
        else:
            self.resultLabel.setText("Check input.")

    def getUI(self, menu):
        menu.setWindowTitle("Cilinder Shape")
        menu.setFixedWidth(500)
        menu.setFixedHeight(275)

        cilinderPicture = QLabel(self)
        cilinderPixMap = QPixmap('assets/cilinder.png')
        cilinderPixMap = cilinderPixMap.scaled(250, 250)
        cilinderPicture.setPixmap(cilinderPixMap)
        cilinderPicture.show()

        self.heightLabel = QLabel(self, text="Height: ")
        self.heightInput = QLineEdit(self)
        self.heightInput.textChanged.connect(self.calculate)

        self.radiusLabel = QLabel(self, text="Radius: ")
        self.radiusInput = QLineEdit(self)
        self.radiusInput.textChanged.connect(self.calculate)

        self.resultLabel = QLabel(self, text="Check input.")

        self.backButton = QPushButton(self, text="Terug")
        self.backButton.clicked.connect(menu.goToMenu)

        layout = QGridLayout()
        layout.addWidget(cilinderPicture, 0, 0, 4, 4)

        layout.addWidget(self.heightLabel, 0, 4)
        layout.addWidget(self.heightInput, 0, 5)
        layout.addWidget(self.radiusLabel, 1, 4)
        layout.addWidget(self.radiusInput, 1, 5)
        layout.addWidget(self.resultLabel, 2, 4, 1, 2)
        layout.addWidget(self.backButton, 3, 4, 1, 2)

        return layout