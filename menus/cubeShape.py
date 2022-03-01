from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QGridLayout, QWidget

from menus.stringFormat import isFloat


class CubeMenu(QWidget):
    def calculate(self):
        self.sizeInput.setText(self.sizeInput.text().replace(",", "."))

        if isFloat(self.sizeInput.text()):
            size = float(self.sizeInput.text())
            self.resultLabel.setText("Inhoud: " + str(size * size * size))
        else:
            self.resultLabel.setText("Check input.")

    def getUI(self, menu):
        menu.setWindowTitle("Cube Shape")
        menu.setFixedWidth(500)
        menu.setFixedHeight(275)

        cubePicture = QLabel(self)
        cubePixMap = QPixmap('assets/cube.png')
        cubePixMap = cubePixMap.scaled(250, 250)
        cubePicture.setPixmap(cubePixMap)
        cubePicture.show()

        self.sizeLabel = QLabel(self, text="Width/Length/Height: ")
        self.sizeInput = QLineEdit(self)
        self.sizeInput.textChanged.connect(self.calculate)

        self.resultLabel = QLabel(self, text="Check input.")

        self.backButton = QPushButton(self, text="Terug")
        self.backButton.clicked.connect(menu.goToMenu)

        layout = QGridLayout()
        layout.addWidget(cubePicture, 0, 0, 3, 3)

        layout.addWidget(self.sizeLabel, 0, 3)
        layout.addWidget(self.sizeInput, 0, 4)
        layout.addWidget(self.resultLabel, 1, 3, 1, 3)
        layout.addWidget(self.backButton, 2, 3, 1, 3)

        return layout