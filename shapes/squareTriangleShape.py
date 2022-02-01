from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QGridLayout, QWidget


class SquareTriangleMenu(QWidget):
    def calculate(self):
        if self.sizeInput.text().isnumeric():
            self.resultLabel.setText("Oppervlakte: " + str(int(self.sizeInput.text()) * int(self.sizeInput.text()) / 2))
        else:
            self.resultLabel.setText("Check input.")

    def getUI(self, menu):
        menu.setWindowTitle("Triangle Shape")
        menu.setFixedWidth(500)
        menu.setFixedHeight(275)

        squareTrianglePicture = QLabel(self)
        squareTrianglePixMap = QPixmap('assets/squareTriangle.png')
        squareTrianglePixMap = squareTrianglePixMap.scaled(250, 250)
        squareTrianglePicture.setPixmap(squareTrianglePixMap)
        squareTrianglePicture.show()

        self.sizeLabel = QLabel(self, text="Width/Height: ")
        self.sizeInput = QLineEdit(self)
        self.sizeInput.textChanged.connect(self.calculate)

        self.resultLabel = QLabel(self, text="Check input.")

        self.backButton = QPushButton(self, text="Terug")
        self.backButton.clicked.connect(menu.goToMenu)

        layout = QGridLayout()
        layout.addWidget(squareTrianglePicture, 0, 0, 3, 3)

        layout.addWidget(self.sizeLabel, 0, 3)
        layout.addWidget(self.sizeInput, 0, 4)
        layout.addWidget(self.resultLabel, 1, 3, 1, 3)
        layout.addWidget(self.backButton, 2, 3, 1, 3)
        return layout