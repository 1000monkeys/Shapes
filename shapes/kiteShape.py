from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLineEdit, QLabel, QPushButton, QGridLayout, QWidget


class KiteMenu(QWidget):
    def calculate(self):
        if self.sizeInput.text().isnumeric():
            self.resultLabel.setText("Oppervlakte: " + str(int(self.sizeInput.text()) * int(self.sizeInput.text())))
        else:
            self.resultLabel.setText("Check input.")

    def getUI(self, menu):
        menu.setWindowTitle("Kite Shape")
        menu.setFixedWidth(500)
        menu.setFixedHeight(275)

        kitePicture = QLabel(self)
        kitePixMap = QPixmap('assets/kite.png')
        kitePixMap = kitePixMap.scaled(250, 250)
        kitePicture.setPixmap(kitePixMap)
        kitePicture.show()

        self.sizeLabel = QLabel(self, text="Width/Height: ")
        self.sizeInput = QLineEdit(self)
        self.sizeInput.textChanged.connect(self.calculate)

        self.resultLabel = QLabel(self, text="Oppervlakte: ")

        self.backButton = QPushButton(self, text="Terug")
        self.backButton.clicked.connect(menu.goToMenu)

        layout = QGridLayout()
        layout.addWidget(kitePicture, 0, 0, 3, 3)

        layout.addWidget(self.sizeLabel, 0, 3)
        layout.addWidget(self.sizeInput, 0, 4)
        layout.addWidget(self.resultLabel, 1, 3, 1, 3)
        layout.addWidget(self.backButton, 2, 3, 1, 3)

        return layout