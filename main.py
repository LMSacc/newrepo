import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton


class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.edit)
        self.tableWidget.cellDoubleClicked.connect(self.edit)
        self.fill_table()

    def fill_table(self):
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(4)
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        data = cur.execute('SELECT * FROM coffee').fetchall()
        for i, t in enumerate(data):
            for j, s in enumerate(t):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(s)))

    def edit(self, row=None, col=None):
        self.ed = EditForm(row, col)
        self.ed.show()


class EditForm(QMainWindow):
    def __init__(self, row, col):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.row, self.col = row, col
        self.initUI()

    def initUI(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    f = Form()
    f.show()
    sys.exit(app.exec())