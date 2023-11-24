import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    f = Form()
    f.show()
    sys.exit(app.exec())
#asdasdasd