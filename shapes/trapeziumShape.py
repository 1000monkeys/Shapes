import math

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QGridLayout, QWidget


class TrapeziumMenu(QWidget):
    def calculate(self):
        if self.upsideInput.text().isnumeric() and self.downsideInput.text().isnumeric() and self.heightInput.text().isnumeric():
            upside = int(self.upsideInput.text())
            downside = int(self.downsideInput.text())
            height = int(self.heightInput.text())

            leftSide = math.sqrt(((downside - upside)/2) * ((downside - upside)/2) + height * height)
            rightSide = math.sqrt(((downside - upside)/2) * ((downside - upside)/2) + height * height)

            self.resultLabel.setText("Oppervlakte: " + str(0.5 * (upside + downside) * height) + "\nOmtrek: " + str(upside + downside + leftSide + rightSide))
        else:
            self.resultLabel.setText("Check input.")

    def getUI(self, menu):
        menu.setWindowTitle("Trapezium Shape")
        menu.setFixedWidth(500)
        menu.setFixedHeight(275)

        trapeziumPicture = QLabel(self)
        trapeziumPixMap = QPixmap('assets/trapezium.png')
        trapeziumPixMap = trapeziumPixMap.scaled(250, 250)
        trapeziumPicture.setPixmap(trapeziumPixMap)
        trapeziumPicture.show()

        self.upsideLabel = QLabel(self, text="Upper side length: ")
        self.upsideInput = QLineEdit(self)
        self.upsideInput.textChanged.connect(self.calculate)

        self.downsideLabel = QLabel(self, text="Bottom side length: ")
        self.downsideInput = QLineEdit(self)
        self.downsideInput.textChanged.connect(self.calculate)

        self.heightLabel = QLabel(self, text="Height: ")
        self.heightInput = QLineEdit(self)
        self.heightInput.textChanged.connect(self.calculate)

        self.resultLabel = QLabel(self, text="Check input.")

        self.backButton = QPushButton(self, text="Terug")
        self.backButton.clicked.connect(menu.goToMenu)

        layout = QGridLayout()
        layout.addWidget(trapeziumPicture, 0, 0, 3, 3)

        layout.addWidget(self.upsideLabel, 0, 4)
        layout.addWidget(self.upsideInput, 0, 5)

        layout.addWidget(self.downsideLabel, 1, 4)
        layout.addWidget(self.downsideInput, 1, 5)

        layout.addWidget(self.heightLabel, 2, 4)
        layout.addWidget(self.heightInput, 2, 5)

        layout.addWidget(self.resultLabel, 3, 4, 2, 2)
        layout.addWidget(self.backButton, 4, 5, 2, 2)

        return layout