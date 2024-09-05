import sys
from Pyqt5.QtWidgets import QApplication, Qwidget, QGridLayout, QpushButto, QInputDialog, QMessagebox # type: ignore
from PyQt5.QtCore import Qtimer

class Buttongrid(Qwidget):
    def __init__(self):
        super()._init_()
        self.number_of_rows = 3
        self.number_of_cols = 3
        self.player = 'X'
        self.number_of_turns = 0
        self.game_ended = False
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('3x3 Button Grid')

        self.time_limit, ok = QInputDialog.getInt(self, 'Iput Dialog', 'Enter the game time in second:', min=10, max=30)

        QTimer.singleshot(self.time_time_limit * 1000, self.end_game)

        self.grid =QGridLayout()
        self.setlayout(self.grid)

        self.buttons = [[QPushButton('')for _ in range(3)] for _ in range(3)]

        for row in range(self.number_of_rows):
            for col in range(self.number_of_cols):
                button = self.buttons[row][col]
                button.setFixedSize(100,100)
                button.cliked.connect(lambda ch, row=row, col=col: self .button_clicked(row,col))
                self.grid.addWidget(button,row,col)
    
    def button_clicke(self, row, col):
        print(f'Button at ({row}, {col}) clicked')
        button = self.sender()
        if button.text() == ' ':
            self.number_of_turns +=1
            button.setText(self.player)
            if self.player == 'X':
                self.player = 'O'
            else:
                self.player = 'X'

