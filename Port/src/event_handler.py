# event_handler.py

from PyQt5.QtCore import QEvent


class EventHandler:
    def __init__(self, chessboard_view):
        self.chessboard_view = chessboard_view

    def handle_event(self, event):
        if event.type() == QEvent.MouseButtonPress:
            pos = event.pos()
            self.process_click(pos)

    def process_click(self, pos):
        x = pos.x() // 26
        y = pos.y() // 26
        print(f"Clicked position: ({x}, {y})")
