from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QGridLayout, QWidget


class PrismaTriangleMenu(QWidget):
    def calculate(self):
        if self.widthInput.text().isnumeric() and self.heightInput.text().isnumeric():
            oppervlakteSmall = int(self.widthInput.text()) * int(self.widthInput.text())
            oppervlakteLarge = oppervlakteSmall / 2 * int(self.heightInput.text())

            length = int(self.heightInput.text())

            self.resultLabel.setText("Oppervlakte: " + str(oppervlakteLarge) +"\nInhoud: " + str(oppervlakteSmall * length))
        else:
            self.resultLabel.setText("Check input.")

    def getUI(self, menu):
        menu.setWindowTitle("Triangle Shape")
        menu.setFixedWidth(500)
        menu.setFixedHeight(275)

        prismaTrianglePicture = QLabel(self)
        prismaTrianglePixMap = QPixmap('assets/prismaTriangle.png')
        prismaTrianglePixMap = prismaTrianglePixMap.scaled(250, 250)
        prismaTrianglePicture.setPixmap(prismaTrianglePixMap)
        prismaTrianglePicture.show()

        self.widthLabel = QLabel(self, text="Width/Height: ")
        self.widthInput = QLineEdit(self)
        self.widthInput.textChanged.connect(self.calculate)

        self.heightLabel = QLabel(self, text="Height: ")
        self.heightInput = QLineEdit(self)
        self.heightInput.textChanged.connect(self.calculate)

        self.resultLabel = QLabel(self, text="Check input.")

        self.backButton = QPushButton(self, text="Terug")
        self.backButton.clicked.connect(menu.goToMenu)

        layout = QGridLayout()
        layout.addWidget(prismaTrianglePicture, 0, 0, 3, 3)

        layout.addWidget(self.widthLabel, 0, 3)
        layout.addWidget(self.widthInput, 0, 4)

        layout.addWidget(self.heightLabel, 1, 3)
        layout.addWidget(self.heightInput, 1, 4)

        layout.addWidget(self.resultLabel, 2, 3, 1, 3)
        layout.addWidget(self.backButton, 3, 3, 1, 3)
        return layout