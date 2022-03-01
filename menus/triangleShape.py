import math

from PyQt5.QtWidgets import QLineEdit, QLabel, QWidget, QHBoxLayout, QVBoxLayout, QPushButton

from PaintWidgets.TrianglePaintWidget import TrianglePaintWidget
from menus.stringFormat import isFloat, isInt


class TriangleMenu(QWidget):
    # self.sizeInput.setText(self.sizeInput.text().replace(",", "."))

    def triangle_exists(a, b, c):
        """Return True iff there exists a triangle with sides a, b, c."""
        return a + b > c and b + c > a and c + a > b

    def calculate(self):
        if isFloat(self.aInput.text()) and isFloat(self.bInput.text()) and isInt(self.oneInput.text()):
            a = float(self.aInput.text())
            b = float(self.bInput.text())
            one = int(self.oneInput.text())

            #print(math.cos(math.radians(one)))

            #c = ((a * a) - (b * b)) + ((2 * b) * math.cos(math.radians(one)))
            c = (a * a) + (b * b) - (2 * a * b * math.cos(math.radians(one)))
            c = math.sqrt(c)
            c = '{:.2f}'.format(c)

            self.cInput.setText(str(c))


        elif isFloat(self.bInput.text()) and isFloat(self.cInput.text()):
            pass
        elif isFloat(self.cInput.text()) and isFloat(self.aInput.text()):
            pass

    def getUI(self, menu):
        self.menu = menu
        self.menu.setWindowTitle("Triangle Shape")

        # label a
        self.aLabel = QLabel(self, text="Side A: ")
        self.aLabel.setFixedWidth(50)
        # input a
        self.aInput = QLineEdit(self)
        self.aInput.setFixedWidth(100)
        # layout a
        self.aHBoxLayout = QHBoxLayout()
        self.aHBoxLayout.addWidget(self.aLabel)
        self.aHBoxLayout.addWidget(self.aInput)

        # label b
        self.bLabel = QLabel(self, text="Side B: ")
        self.bLabel.setFixedWidth(50)
        # input b
        self.bInput = QLineEdit(self)
        self.bInput.setFixedWidth(100)
        # layout b
        self.bHBoxLayout = QHBoxLayout()
        self.bHBoxLayout.addWidget(self.bLabel)
        self.bHBoxLayout.addWidget(self.bInput)

        # label c
        self.cLabel = QLabel(self, text="Side C: ")
        self.cLabel.setFixedWidth(50)
        # input c
        self.cInput = QLineEdit(self)
        self.cInput.setFixedWidth(100)
        # layout c
        self.cHBoxLayout = QHBoxLayout()
        self.cHBoxLayout.addWidget(self.cLabel)
        self.cHBoxLayout.addWidget(self.cInput)

        # label 1
        self.oneLabel = QLabel(self, text="Corner 1 in degrees: ")
        self.oneLabel.setFixedWidth(100)
        # input 1
        self.oneInput = QLineEdit(self)
        self.oneInput.setFixedWidth(50)
        # layout 1
        self.oneHBoxLayout = QHBoxLayout()
        self.oneHBoxLayout.addWidget(self.oneLabel)
        self.oneHBoxLayout.addWidget(self.oneInput)

        # label 2
        self.twoLabel = QLabel(self, text="Corner 2 in degrees: ")
        self.twoLabel.setFixedWidth(100)
        # input 2
        self.twoInput = QLineEdit(self)
        self.twoInput.setFixedWidth(50)
        # layout 2
        self.twoHBoxLayout = QHBoxLayout()
        self.twoHBoxLayout.addWidget(self.twoLabel)
        self.twoHBoxLayout.addWidget(self.twoInput)

        # label 3
        self.threeLabel = QLabel(self, text="Corner 3 in degrees: ")
        self.threeLabel.setFixedWidth(100)
        # input 3
        self.threeInput = QLineEdit(self)
        self.threeInput.setFixedWidth(50)
        # layout 3
        self.threeHBoxLayout = QHBoxLayout()
        self.threeHBoxLayout.addWidget(self.threeLabel)
        self.threeHBoxLayout.addWidget(self.threeInput)

        # Calculate button
        self.calculateButton = QPushButton("Calculate", self)
        self.calculateButton.setFixedWidth(150)
        self.calculateButton.clicked.connect(self.calculate)

        # Clear button
        self.clearButton = QPushButton("Clear", self)
        self.clearButton.setFixedWidth(150)

        # Info label
        infoText = "INFO:\n" \
                    "Three of the input's\n" \
                   "need to be filled to\n" \
                   "calculate the other three!"
        self.infoLabel = QLabel(self, text=infoText)
        self.infoLabel.setFixedWidth(150)

        # Button
        self.buttonInfoVBoxLayout = QVBoxLayout()
        self.buttonInfoVBoxLayout.addWidget(self.calculateButton)
        self.buttonInfoVBoxLayout.addWidget(self.infoLabel)
        self.buttonInfoVBoxLayout.addWidget(self.clearButton)

        # layout on the right side with the inputs
        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addLayout(self.aHBoxLayout)
        self.vBoxLayout.addLayout(self.bHBoxLayout)
        self.vBoxLayout.addLayout(self.cHBoxLayout)
        self.vBoxLayout.addLayout(self.oneHBoxLayout)
        self.vBoxLayout.addLayout(self.twoHBoxLayout)
        self.vBoxLayout.addLayout(self.threeHBoxLayout)

        self.vBoxLayout.addLayout(self.buttonInfoVBoxLayout)


        # Layout containing the paintwidget and the layout with the inputs
        self.hBoxLayout = QHBoxLayout()
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.addWidget(TrianglePaintWidget(self))
        self.hBoxLayout.addLayout(self.vBoxLayout)

        # DEBUG
        self.aInput.setText("3")
        self.bInput.setText("4")
        self.oneInput.setText("90")

        return self.hBoxLayout
