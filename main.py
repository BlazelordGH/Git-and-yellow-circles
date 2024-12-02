import sys#а

from PyQt6 import uic, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QColor


class YellowCirclesApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.draw_btn.clicked.connect(self.click)
        self.clear_screen()
        self.draw_walls()

    def click(self):
        self.clear_screen()
        self.draw_circles()
        self.draw_walls()

    def clear_screen(self):
        canvas = QtGui.QPixmap(780, 450)
        canvas.fill(QColor(128, 0, 128))
        self.draw_label.setPixmap(canvas)

    def draw_circles(self):
        from random import randint

        canvas = self.draw_label.pixmap()
        painter = QtGui.QPainter(canvas)

        pen = QtGui.QPen()
        pen.setWidth(4)

        colors = [[0, 0, 0], [255, 128, 128],
                  [100, 100, 100], [255, 0, 255],
                  [192, 0, 56], [0, 255, 0],
                  [255, 255, 0], [128, 255, 0]]
        for i in range(randint(5, 50)):
            colors_index = randint(0, len(colors) - 1)
            pen.setColor(QColor(colors[colors_index][0], colors[colors_index][1], colors[colors_index][2]))
            painter.setPen(pen)

            diameter = randint(10, 50)
            x, y = randint(20, 780 - diameter - 20), randint(20, 450 - diameter - 20)
            painter.drawEllipse(x, y, diameter, diameter)

        painter.end()
        self.draw_label.setPixmap(canvas)

    def draw_walls(self):
        canvas = self.draw_label.pixmap()
        painter = QtGui.QPainter(canvas)

        pen = QtGui.QPen()
        pen.setWidth(20)
        pen.setColor(QtGui.QColor('black'))
        painter.setPen(pen)
        painter.drawLine(0, 0, 780, 0)
        painter.drawLine(0, 450, 780, 450)
        painter.drawLine(0, 0, 0, 450)
        painter.drawLine(780, 0, 780, 450)
        painter.end()

        self.draw_label.setPixmap(canvas)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    yellowCirclesApp = YellowCirclesApp()
    yellowCirclesApp.show()
    sys.exit(app.exec())
