from PyQt5.QtWidgets import QApplication
import sys

from combinational_sum.gui.window import MainWindow


class App:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = MainWindow()

    def run(self):
        self.main_window.show()
        return self.app.exec_()
