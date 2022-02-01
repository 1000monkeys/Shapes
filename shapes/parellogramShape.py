from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QGridLayout, QWidget


class ParellogramMenu(QWidget):
    def calculate(self):
        if self.sideInput.text().isnumeric() and self.heightInput.text().isnumeric():
            self.resultLabel.setText("Oppervlakte: " + str(int(self.sideInput.text()) * int(self.heightInput.text())))
        else:
            self.resultLabel.setText("Check input.")

    def getUI(self, menu):
        menu.setWindowTitle("Parellogram Shape")
        menu.setFixedWidth(500)
        menu.setFixedHeight(275)

        parellogramPicture = QLabel(self)
        parellogramPixMap = QPixmap('assets/parellogram.png')
        parellogramPixMap = parellogramPixMap.scaled(250, 250)
        parellogramPicture.setPixmap(parellogramPixMap)
        parellogramPicture.show()

        self.sideLabel = QLabel(self, text="Bovenste/Onderste zijde: ")
        self.sideInput = QLineEdit(self)
        self.sideInput.textChanged.connect(self.calculate)

        self.heightLabel = QLabel(self, text="Hoogte: ")
        self.heightInput = QLineEdit(self)
        self.heightInput.textChanged.connect(self.calculate)

        self.resultLabel = QLabel(self, text="Check input.")

        self.backButton = QPushButton(self, text="Terug")
        self.backButton.clicked.connect(menu.goToMenu)

        layout = QGridLayout()
        layout.addWidget(parellogramPicture, 0, 0, 4, 4)

        layout.addWidget(self.sideLabel, 0, 4)
        layout.addWidget(self.sideInput, 0, 5)

        layout.addWidget(self.heightLabel, 1, 4)
        layout.addWidget(self.heightInput, 1, 5)

        layout.addWidget(self.resultLabel, 2, 4, 1, 2)
        layout.addWidget(self.backButton, 3, 4, 1, 2)

        return layout