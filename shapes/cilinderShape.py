import math

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QGridLayout, QWidget


class CilinderMenu(QWidget):
    def calculate(self):
        if self.sizeInput.text().isnumeric() and self.radiusInput.text().isnumeric():
            self.resultLabel.setText("Inhoud: " + str(int(self.radiusInput.text()) * math.pi * int(self.sizeInput.text())))
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

        self.sizeLabel = QLabel(self, text="Height: ")
        self.sizeInput = QLineEdit(self)
        self.sizeInput.textChanged.connect(self.calculate)

        self.radiusLabel = QLabel(self, text="Radius: ")
        self.radiusInput = QLineEdit(self)
        self.radiusInput.textChanged.connect(self.calculate)

        self.resultLabel = QLabel(self, text="Inhoud: ")

        self.backButton = QPushButton(self, text="Terug")
        self.backButton.clicked.connect(menu.goToMenu)

        layout = QGridLayout()
        layout.addWidget(cilinderPicture, 0, 0, 4, 4)

        layout.addWidget(self.sizeLabel, 0, 4)
        layout.addWidget(self.sizeInput, 0, 5)
        layout.addWidget(self.radiusLabel, 1, 4)
        layout.addWidget(self.radiusInput, 1, 5)
        layout.addWidget(self.resultLabel, 2, 4, 1, 2)
        layout.addWidget(self.backButton, 3, 4, 1, 2)

        return layout