from PyQt5.QtGui import QColor, QBrush, QPixmap
from PyQt5.QtCore import QRectF
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView


class JavaXQ:
    def __init__(self):
        self.cx = 26
        self.cy = 26
        self.boardW = 247
        self.boardH = 299
        self.foreColor = QColor("white")
        self.backColor = QColor(153, 204, 153)
        self.pieceInitXY = [100] * 32
        self.pieceCurrXY = [100] * 32
        self.pieceName = "RHEAKAEHRCCPPPPPrheakaehrccppppp"
        self.stepNo = 0
        self.stepNum = 0
        self.isRedAtBottom = True
        self.stepListXYf = [0] * 512
        self.stepListXYt = [0] * 512

    def draw_piece(self, painter, piece_char, x_pos, y_pos):
        if self.isRedAtBottom:
            y_pos = 9 - y_pos
        else:
            x_pos = 8 - x_pos

        x = 20 + self.cx * x_pos - self.cx // 2 + 1
        y = 20 + self.cy * y_pos - self.cy // 2 + 1

        painter.setBrush(QBrush(QColor("blue")))
        painter.drawEllipse(x, y, 24, 24)
        painter.setBrush(QBrush(QColor("white")))
        # Add specific rendering logic for each piece

    def draw_board(self, painter):
        painter.setBrush(QBrush(self.backColor))
        painter.drawRect(0, 0, self.boardW, self.boardH)
        painter.setBrush(QBrush(self.foreColor))
        # Draw horizontal and vertical lines
        for i in range(10):
            painter.drawLine(0, i * self.cy, 8 * self.cx, i * self.cy)
        for i in range(9):
            painter.drawLine(i * self.cx, 0, i * self.cx, 9 * self.cy)

    def draw_position(self, painter):
        for i in range(32):
            self.pieceCurrXY[i] = self.pieceInitXY[i]

        for step in range(self.stepNo):
            for i in range(32):
                if self.pieceCurrXY[i] == self.stepListXYt[step]:
                    self.pieceCurrXY[i] = 100
                if self.pieceCurrXY[i] == self.stepListXYf[step]:
                    self.pieceCurrXY[i] = self.stepListXYt[step]

        for i in range(32):
            if self.pieceCurrXY[i] > 89:
                continue
            self.draw_piece(
                painter,
                self.pieceName[i],
                self.pieceCurrXY[i] // 10,
                self.pieceCurrXY[i] % 10,
            )

    def init_position(self, position_param):
        if not position_param:
            position_param = "I0,H0,G0,F0,E0,D0,C0,B0,A0,H2,B2,I3,G3,E3,C3,A3|A9,B9,C9,D9,E9,F9,G9,H9,I9,B7,H7,A6,C6,E6,G6,I6"
        positions = position_param.split("|")
        for i, pos in enumerate(positions[0].split(",")):
            self.pieceInitXY[i] = int(pos[1]) * 10 + ord(pos[0]) - ord("A")

    def init_move_list(self, move_list_param):
        if move_list_param:
            steps = move_list_param.split(",")
            for i, step in enumerate(steps):
                from_pos, to_pos = step.split("-")
                self.stepListXYf[i] = int(from_pos)
                self.stepListXYt[i] = int(to_pos)
            self.stepNum = len(steps)

    def paint(self, painter):
        self.draw_board(painter)
        self.draw_position(painter)
