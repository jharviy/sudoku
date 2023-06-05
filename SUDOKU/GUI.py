

#from PyQt6 import *
from PyQt6.QtWidgets import (
    QApplication, QWidget, QTableWidget, QTableWidgetItem
)
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sudoku')

app = QApplication(sys.argv)
abc = Window()
abc.show()
#app.exec()
sys.exit(app.exec())