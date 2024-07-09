from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
        QHBoxLayout, QVBoxLayout,
        QGroupBox, QRadioButton,
        QPushButton, QLabel,  QLineEdit)

    
from instr import *
from second_win import *

class MainWin(QWidget):
    def __int__(self):
        super().__init__()
        self.connect()
        self.set_appear()
        self.show()

    def initUI(self):
        self.btn_next = QPushButton(txt_next, self)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)

        self.l_line = QVBoxLayout()
        self.l_line.addWidget(self.hello_text, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.instruction, alignment= Qt.AlignLeft)
        self.l_line.addWidget(self.btn_next, alignment= Qt.AlignCenter)
        self.setLayout(self.l_line)
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def next_click(self):
        self.hide()
        self.tw = TestWin()
    def connect(self):
        self.btn_next.clicked.connect(self.next_click)
app = QApplication([])
mw = MainWin()
app.exec_()
