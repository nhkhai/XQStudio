# chessboard.py

from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QBrush, QColor


class ChessPieceRenderer:
    def __init__(self):
        self.piece_name = "RHEAKAEHRCCPPPPPrheakaehrccppppp"
        self.piece_positions = [100] * 32

    def render_piece(self, painter, piece_char, x_pos, y_pos):
        x = 20 + 26 * x_pos - 26 // 2 + 1
        y = 20 + 26 * y_pos - 26 // 2 + 1

        painter.setBrush(QBrush(QColor("blue")))
        painter.drawEllipse(x, y, 24, 24)
        painter.setBrush(QBrush(QColor("white")))
        # Add specific rendering logic for each piece


class Chessboard(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.piece_renderer = ChessPieceRenderer()

    def draw_position(self, painter):
        for i, pos in enumerate(self.piece_renderer.piece_positions):
            if pos > 89:
                continue
            x_pos = pos // 10
            y_pos = pos % 10
            self.piece_renderer.render_piece(
                painter, self.piece_renderer.piece_name[i], x_pos, y_pos
            )


class ChessboardView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = Chessboard()
        self.setScene(self.scene)
