import sys
import aecf
import mainUI
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton, QLineEdit


class Form(QMainWindow, mainUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.edit)
        self.tableWidget.cellDoubleClicked.connect(self.edit)
        self.fill_table()

    def fill_table(self):
        self.tableWidget.setColumnCount(7)
        con = sqlite3.connect('data/coffee.sqlite')
        cur = con.cursor()
        data = cur.execute('SELECT * FROM coffee').fetchall()
        titles = list(x[1] for x in cur.execute(f'PRAGMA table_info(coffee)').fetchall())
        self.tableWidget.setHorizontalHeaderLabels(titles)
        self.tableWidget.setRowCount(len(data))
        for i, t in enumerate(data):
            for j, s in enumerate(t):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(s)))
        con.close()

    def edit(self, row=None, col=None):
        self.ed = EditForm(row, col, self.tableWidget)
        self.ed.show()


class EditForm(QMainWindow, aecf.Ui_MainWindow):
    def __init__(self, row, col, tw):
        super().__init__()
        self.setupUi(self)
        self.row, self.col, self.tw = row, col, tw
        self.lineEdit = QLineEdit(self)
        self.lineEdit.resize(200, 30)
        if isinstance(self.sender(), QPushButton):
            self.pushButton.clicked.connect(self.add_row)
        else:
            self.pushButton.clicked.connect(self.change)

    def add_row(self):
        self.tw.setRowCount(self.tw.rowCount() + 1)
        txt = self.lineEdit.text().split(';')
        for i in range(7):
            self.tw.setItem(self.tw.rowCount() - 1, i, QTableWidgetItem(txt[i]))
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        cur.execute(
            f"""
        INSERT INTO coffee("ID", "Название", "Обжарка", "Молотый", "Вкус", "Цена", "Объём")
        VALUES({', '.join(f"'{i}'" for i in txt)})
            """)
        con.commit()
        con.close()

    def change(self):
        self.tw.setItem(self.row, self.col, QTableWidgetItem(self.lineEdit.text()))
        cond = ' AND '.join([
            f"{key} = '{val}'" for key, val in
            {self.tw.horizontalHeaderItem(i).text(): self.tw.item(self.row, i).text()
             for i in range(self.tw.columnCount())
             if self.tw.item(self.row, i).text() != self.lineEdit.text()}.items()
        ])
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        cur.execute(f"""
        UPDATE coffee
        SET {list(x[1] for x in cur.execute(f'PRAGMA table_info(coffee)').fetchall())[self.col]} =
        '{self.lineEdit.text()}'
        WHERE {cond}
""")
        con.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    f = Form()
    f.show()
    sys.exit(app.exec())