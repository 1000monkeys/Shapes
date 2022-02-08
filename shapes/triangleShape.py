from PyQt5.QtCore import Qt, QRect, QSize
from PyQt5.QtWidgets import QLineEdit, QLabel, QGridLayout, QWidget, QHBoxLayout, QVBoxLayout

from PaintWidgets.TrianglePaintWidget import TrianglePaintWidget


class TriangleMenu(QWidget):
    def calculate(self):
        self.sizeInput.setText(self.sizeInput.text().replace(",", "."))

        if self.sizeInput.text().isnumeric():
            self.resultLabel.setText("Oppervlakte: " + str(float(self.sizeInput.text()) * float(self.sizeInput.text()) / 2))
        else:
            self.resultLabel.setText("Check input.")

    def getUI(self, menu):
        self.menu = menu
        self.menu.setWindowTitle("Triangle Shape")
        #self.menu.setFixedWidth(500)
        #self.menu.setFixedHeight(275)

        """
        trianglePicture = QLabel(self)
        trianglePixMap = QPixmap('assets/triangle.png')
        trianglePixMap = trianglePixMap.scaled(250, 250)
        trianglePicture.setPixmap(trianglePixMap)
        trianglePicture.show()

        self.sizeLabel = QLabel(self, text="Width/Height: ")
        self.sizeInput = QLineEdit(self)
        self.sizeInput.textChanged.connect(self.calculate)

        self.resultLabel = QLabel(self, text="Check input.")

        self.backButton = QPushButton(self, text="Terug")
        self.backButton.clicked.connect(menu.goToMenu)

        layout = QGridLayout()
        layout.addWidget(trianglePicture, 0, 0, 3, 3)

        layout.addWidget(self.sizeLabel, 0, 3)
        layout.addWidget(self.sizeInput, 0, 4)
        layout.addWidget(self.resultLabel, 1, 3, 1, 3)
        layout.addWidget(self.backButton, 2, 3, 1, 3)
        """
        self.sizeLabel = QLabel(self, text="Height: ")
        self.sizeLabel.setFixedWidth(50)

        self.sizeInput = QLineEdit(self)
        self.sizeInput.setFixedWidth(100)
        self.sizeInput.textChanged.connect(self.calculate)

        self.sizeHBoxLayout = QHBoxLayout()
        self.sizeHBoxLayout.addWidget(self.sizeLabel)
        self.sizeHBoxLayout.addWidget(self.sizeInput)

        self.heightLabel = QLabel(self, text="Height: ")
        self.heightLabel.setFixedWidth(50)

        self.heightInput = QLineEdit(self)
        self.heightInput.setFixedWidth(100)
        self.heightInput.textChanged.connect(self.calculate)

        self.heightHBoxLayout = QHBoxLayout()
        self.heightHBoxLayout.addWidget(self.heightLabel)
        self.heightHBoxLayout.addWidget(self.heightInput)

        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addLayout(self.sizeHBoxLayout)
        self.vBoxLayout.addLayout(self.heightHBoxLayout)

        self.hBoxLayout = QHBoxLayout()
        self.hBoxLayout.addWidget(TrianglePaintWidget(self))
        self.hBoxLayout.addLayout(self.vBoxLayout)

        return self.hBoxLayout
