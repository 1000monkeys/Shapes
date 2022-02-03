from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QGridLayout, QWidget

from shapes.isFloat import isFloat


class SquareMenu(QWidget):
    def calculate(self):
        self.sizeInput.setText(self.sizeInput.text().replace(",", "."))

        if isFloat(self.sizeInput.text()):
            self.resultLabel.setText("Oppervlakte: " + str(float(self.sizeInput.text()) * float(self.sizeInput.text())))
        else:
            self.resultLabel.setText("Check input.")

    def getUI(self, menu):
        menu.setWindowTitle("Square Shape")
        menu.setFixedWidth(500)
        menu.setFixedHeight(275)

        squarePicture = QLabel(self)
        squarePixMap = QPixmap('assets/square.png')
        squarePixMap = squarePixMap.scaled(250, 250)
        squarePicture.setPixmap(squarePixMap)
        squarePicture.show()

        self.sizeLabel = QLabel(self, text="Width/Height: ")
        self.sizeInput = QLineEdit(self)
        self.sizeInput.textChanged.connect(self.calculate)

        self.resultLabel = QLabel(self, text="Check input.")

        self.backButton = QPushButton(self, text="Terug")
        self.backButton.clicked.connect(menu.goToMenu)

        layout = QGridLayout()
        layout.addWidget(squarePicture, 0, 0, 3, 3)

        layout.addWidget(self.sizeLabel, 0, 3)
        layout.addWidget(self.sizeInput, 0, 4)
        layout.addWidget(self.resultLabel, 1, 3, 1, 3)
        layout.addWidget(self.backButton, 2, 3, 1, 3)

        return layout