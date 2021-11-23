import sys
import time


from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randrange, randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False
        self.num = 1

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        working = True
        while True:
            self.do_paint = True
            self.repaint()
            time.sleep(0.5)

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        x_y = randint(40, 150)
        qp.drawEllipse(randrange(500), randrange(200), x_y, x_y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())