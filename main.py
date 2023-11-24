import sys
import random
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.drawCircles)
        self.draw = False
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.resize(300, 300)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Нажми!"))

    def drawCircles(self):
        self.draw = True
        self.repaint()

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            r = random.randint(10, 100)
            qp.drawEllipse(random.randint(10, 200), random.randint(10, 200), r, r)
            qp.end()
            self.draw = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    f = Form()
    f.show()
    sys.exit(app.exec())
