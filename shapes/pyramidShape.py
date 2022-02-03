from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QGridLayout, QWidget

from shapes.isFloat import isFloat


class PyramidMenu(QWidget):
    def calculate(self):
        self.widthInput.setText(self.widthInput.text().replace(",", "."))
        self.heightInput.setText(self.heightInput.text().replace(",", "."))

        if isFloat(self.heightInput.text()) and isFloat(self.widthInput.text()):
            self.resultLabel.setText(
                "Inhoud: " + str(float(self.heightInput.text()) * float(self.widthInput.text()) / 2))
        else:
            self.resultLabel.setText("Check input.")

    def getUI(self, menu):
        menu.setWindowTitle("Pyramid Shape")
        menu.setFixedWidth(500)
        menu.setFixedHeight(275)

        pyramidPicture = QLabel(self)
        pyramidPixMap = QPixmap('assets/pyramid.png')
        pyramidPixMap = pyramidPixMap.scaled(250, 250)
        pyramidPicture.setPixmap(pyramidPixMap)
        pyramidPicture.show()

        self.heightLabel = QLabel(self, text="Height: ")
        self.heightInput = QLineEdit(self)
        self.heightInput.textChanged.connect(self.calculate)

        self.widthLabel = QLabel(self, text="Width: ")
        self.widthInput = QLineEdit(self)
        self.widthInput.textChanged.connect(self.calculate)

        self.resultLabel = QLabel(self, text="Check input.")

        self.backButton = QPushButton(self, text="Terug")
        self.backButton.clicked.connect(menu.goToMenu)

        layout = QGridLayout()
        layout.addWidget(pyramidPicture, 0, 0, 4, 4)

        layout.addWidget(self.heightLabel, 0, 4, 1, 2)
        layout.addWidget(self.heightInput, 0, 5, 1, 2)

        layout.addWidget(self.widthLabel, 1, 4, 1, 2)
        layout.addWidget(self.widthInput, 1, 5, 1, 2)

        layout.addWidget(self.resultLabel, 2, 4, 1, 4)
        layout.addWidget(self.backButton, 3, 4, 1, 4)

        return layout