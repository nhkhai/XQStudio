from PyQt5.QtGui import QColor, QBrush
from PyQt5.QtWidgets import QGraphicsScene


class ChessboardRenderer(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.piece_name = "RHEAKAEHRCCPPPPPrheakaehrccppppp"
        self.piece_positions = [100] * 32

    def draw_piece(self, painter, piece_char, x_pos, y_pos):
        x = 20 + 26 * x_pos - 26 // 2 + 1
        y = 20 + 26 * y_pos - 26 // 2 + 1

        painter.setBrush(QBrush(QColor("blue")))
        painter.drawEllipse(x, y, 24, 24)
        painter.setBrush(QBrush(QColor("white")))
        # Add specific rendering logic for each piece

    def draw_position(self, painter):
        for i, pos in enumerate(self.piece_positions):
            if pos > 89:
                continue
            x_pos = pos // 10
            y_pos = pos % 10
            self.draw_piece(painter, self.piece_name[i], x_pos, y_pos)
