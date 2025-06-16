from PyQt5.QtGui import QColor, QBrush


class ChessPieceRenderer:
    def __init__(self):
        self.piece_name = "RHEAKAEHRCCPPPPPrheakaehrccppppp"

    def render_piece(self, scene, piece_char, x_pos, y_pos):
        x = 20 + 26 * x_pos - 26 // 2 + 1
        y = 20 + 26 * y_pos - 26 // 2 + 1

        if piece_char == 'K':
            self.draw_red_k(scene, x, y)
        elif piece_char == 'E':
            self.draw_blk_e(scene, x, y)
        else:
            scene.addEllipse(x, y, 24, 24, QColor("gray"))

    def draw_red_k(self, painter, x, y):
        painter.setBrush(QBrush(QColor("red")))
        painter.drawEllipse(x, y, 24, 24)
        painter.setPen(QColor("white"))
        painter.drawLine(x + 14, y + 4, x + 14, y + 19)
        painter.drawLine(x + 15, y + 4, x + 15, y + 5)
        painter.drawLine(x + 12, y + 8, x + 18, y + 8)
        painter.drawLine(x + 11, y + 9, x + 11, y + 14)
        painter.drawLine(x + 12, y + 9, x + 12, y + 10)
        painter.drawLine(x + 17, y + 9, x + 18, y + 9)
        painter.drawLine(x + 17, y + 10, x + 17, y + 15)
        painter.drawLine(x + 15, y + 14, x + 16, y + 14)
        painter.drawLine(x + 16, y + 15, x + 16, y + 15)

    def draw_blk_e(self, painter, x, y):
        painter.setBrush(QBrush(QColor("blue")))
        painter.drawEllipse(x, y, 24, 24)
        painter.setPen(QColor("white"))
        painter.drawLine(x + 9, y + 3, x + 9, y + 3)
        painter.drawLine(x + 10, y + 4, x + 10, y + 4)
        painter.drawLine(x + 9, y + 5, x + 9, y + 7)
        painter.drawLine(x + 8, y + 8, x + 11, y + 8)
        painter.drawRect(x + 5, y + 9, 5, 2)
        painter.drawLine(x + 10, y + 9, x + 10, y + 9)
        painter.drawRect(x + 8, y + 11, 2, 9)
        painter.drawLine(x + 10, y + 11, x + 10, y + 12)
        painter.drawLine(x + 7, y + 12, x + 7, y + 13)
        painter.drawLine(x + 6, y + 14, x + 6, y + 14)
        painter.drawLine(x + 5, y + 15, x + 5, y + 15)
        painter.drawLine(x + 4, y + 16, x + 4, y + 16)
        painter.drawRect(x + 12, y + 9, 2, 6)
        painter.drawLine(x + 12, y + 15, x + 12, y + 16)
        painter.drawLine(x + 14, y + 8, x + 16, y + 8)
        painter.drawRect(x + 17, y + 8, 2, 11)
        painter.drawLine(x + 15, y + 10, x + 15, y + 10)
        painter.drawLine(x + 14, y + 11, x + 15, y + 11)
        painter.drawLine(x + 14, y + 13, x + 15, y + 13)
        painter.drawLine(x + 13, y + 16, x + 15, y + 16)
        painter.drawLine(x + 16, y + 17, x + 16, y + 17)
        painter.drawLine(x + 18, y + 18, x + 18, y + 18)
        # Add specific rendering logic for Black Elephant

    # Add other piece rendering methods as needed
