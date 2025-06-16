from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel
from chessboard_renderer import ChessboardRenderer
from event_handler import EventHandler
from position_initializer import PositionInitializer
from move_list_handler import MoveListHandler
from bitmap_loader import BitmapLoader


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("XQStudio 1.63")

        # Initialize handlers
        self.move_list_handler = MoveListHandler()
        self.bitmap_loader = BitmapLoader()
        self.event_handler = EventHandler(self)
        self.position_initializer = PositionInitializer()

        # Main layout
        layout = QVBoxLayout()

        # Add chessboard view
        self.chessboard_view = ChessboardRenderer()
        layout.addWidget(self.chessboard_view)

        # Add widgets
        self.label = QLabel("Welcome to XQStudio")
        layout.addWidget(self.label)

        self.about_button = QPushButton("About")
        self.about_button.clicked.connect(self.show_about)
        layout.addWidget(self.about_button)

        self.wizard_button = QPushButton("Wizard")
        self.wizard_button.clicked.connect(self.show_wizard)
        layout.addWidget(self.wizard_button)

        self.tips_button = QPushButton("Tips")
        self.tips_button.clicked.connect(self.show_tips)
        layout.addWidget(self.tips_button)

        # Set central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def show_about(self):
        print("About dialog")

    def show_wizard(self):
        print("Wizard dialog")

    def show_tips(self):
        print("Tips dialog")
