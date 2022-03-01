import math

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QGridLayout, QWidget

from menus.stringFormat import isFloat


class CircleMenu(QWidget):
    def calculate(self):
        self.radiusInput.setText(self.radiusInput.text().replace(",", "."))

        if isFloat(self.radiusInput.text()):
            radius = float(self.radiusInput.text())

            self.resultLabel.setText("Oppervlakte: " +
                str(radius * radius * math.pi) + "\nOmtrek: " +
                str(radius * 2 * math.pi))
        else:
            self.resultLabel.setText("Check input.")

    def getUI(self, menu):
        menu.setWindowTitle("Circle Shape")
        menu.setFixedWidth(500)
        menu.setFixedHeight(275)

        circlePicture = QLabel(self)
        circlePixMap = QPixmap('assets/circle.png')
        circlePixMap = circlePixMap.scaled(250, 250)
        circlePicture.setPixmap(circlePixMap)
        circlePicture.show()

        self.radiusLabel = QLabel(self, text="Radius: ")
        self.radiusInput = QLineEdit(self)
        self.radiusInput.textChanged.connect(self.calculate)

        self.resultLabel = QLabel(self, text="Check input.")

        self.backButton = QPushButton(self, text="Terug")
        self.backButton.clicked.connect(menu.goToMenu)


        layout = QGridLayout()
        layout.addWidget(circlePicture, 0, 0, 3, 3)

        layout.addWidget(self.radiusLabel, 0, 3)
        layout.addWidget(self.radiusInput, 0, 4)
        layout.addWidget(self.resultLabel, 1, 3, 1, 3)
        layout.addWidget(self.backButton, 2, 3, 1, 3)

        return layout