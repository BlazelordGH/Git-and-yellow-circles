import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class YellowCirclesApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.draw_btn.clicked.connect(self.click)
        self.show()

    def click(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    yellowCirclesApp = YellowCirclesApp()
    sys.exit(app.exec())
