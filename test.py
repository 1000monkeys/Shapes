import sys
from PyQt5.QtWidgets import QWidget, QPushButton,QHBoxLayout, QGridLayout, QApplication

class UI(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.addButton = QPushButton("add")
        #once click the addButton, call add() function
        self.addButton.clicked.connect(self.add)

        self.delButton = QPushButton("delete")
        self.delButton.clicked.connect(self.deleteItemsOfLayout)

        self.layout = QGridLayout()
        self.layout.addWidget(self.addButton, 0, 0)
        self.layout.addWidget(self.delButton, 0, 1)

        self.setLayout(self.layout)

        self.setWindowTitle('add')
        self.show()

    def add(self):

        Button1 = QPushButton("1")
        Button2 = QPushButton("2")

        self.added = QGridLayout()
        self.added.addWidget(Button1, 0, 0)
        self.added.addWidget(Button2, 0, 1)

        self.layout.addLayout(self.added, 1, 0)

    #this will not work with layout
    def delete(self):
        self.layout.itemAt(2).layout().deleteLater()

    #
    def deleteItemsOfLayout(self):
        #first check whether the layout we want to delete exists
        if self.layout.count() > 2:
            #delete each widget in the layout one by one
            while self.added.count():
                item = self.added.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    #two ways to delete widgets
                    #widget.setParent(None)
                    widget.deleteLater()
                else:
                    deleteItemsOfLayout(item.layout())
        else:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())