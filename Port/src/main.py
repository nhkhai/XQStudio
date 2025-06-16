import sys

from PyQt5.QtCore import QEvent, QRectF
from PyQt5.QtGui import QColor, QBrush, QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QTabWidget, \
    QGraphicsScene, QGraphicsView

from position_initializer import PositionInitializer
from tips import TipsDialog
from wizard import WizardDialog

BACKGROUND_COLOR = "background-color: #f0f0f0;"


class ChessPieceRenderer:
    def __init__(self):
        self.piece_name = "RHEAKAEHRCCPPPPPrheakaehrccppppp"
        self.piece_positions = [100] * 32
        self.is_red_at_bottom = True  # Defined missing attribute

    def render_piece(self, x_pos, y_pos):
        # Removed unused painter parameter and variables x, y
        pass

    def draw_piece(self, painter, piece_char, x_pos, y_pos):
        if self.is_red_at_bottom:
            y_pos = 9 - y_pos
        else:
            x_pos = 8 - x_pos

        x = 20 + 26 * x_pos - 26 // 2 + 1
        y = 20 + 26 * y_pos - 26 // 2 + 1

        painter.setBrush(QBrush(QColor("blue")))
        painter.drawEllipse(x, y, 24, 24)
        painter.setFont(QFont("Arial", 12, QFont.Bold))  # Set font for the text
        painter.setPen(QColor("white"))  # Set pen color for text
        painter.drawText(x + 6, y + 18, piece_char)  # Draw the piece character

        self.is_red_at_bottom = True


class Chessboard(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.piece_renderer = ChessPieceRenderer()
        self.is_red_at_bottom = True  # Ensure this attribute is defined
        self.setSceneRect(0, 0, 732, 454)  # Set chessboard dimensions

    def draw_board(self):
        # Draw border
        self.addRect(QRectF(3, 3, 732 - 6, 454 - 6), brush=QBrush(QColor("gray")))
        self.addRect(QRectF(4, 4, 732 - 6, 454 - 6), brush=QBrush(QColor("white")))

        # Draw horizontal lines
        for i in range(10):
            self.addLine(20, 20 + i * 26, 20 + 8 * 26, 20 + i * 26, QColor("black"))

        # Draw vertical lines
        for i in range(9):
            self.addLine(20 + i * 26, 20, 20 + i * 26, 20 + 4 * 26, QColor("black"))
            self.addLine(20 + i * 26, 20 + 5 * 26, 20 + i * 26, 20 + 9 * 26, QColor("black"))

    def initialize_pieces(self):
        # Initialize pieces on the board
        print("Initializing pieces...")
        self.piece_renderer.piece_positions = [
            40, 41, 42, 43, 44, 45, 46, 47, 48, 49,  # Red pieces
            30, 31, 32, 33, 34, 35, 36, 37, 38, 39,  # Black pieces
        ]
        self.piece_renderer.piece_name = "RHEAKAEHRCCPPPPPrheakaehrccppppp"

        for i, pos in enumerate(self.piece_renderer.piece_positions):
            if pos > 89:
                continue
            x_pos = pos // 10
            y_pos = pos % 10

            # Use addEllipse for rendering pieces instead of QPainter
            x = 20 + 26 * x_pos - 26 // 2 + 1
            y = 20 + 26 * y_pos - 26 // 2 + 1

            ellipse = self.addEllipse(x, y, 24, 24, QColor("blue"), QBrush(QColor("blue")))
            text = self.addText(self.piece_renderer.piece_name[i], QFont("Arial", 12, QFont.Bold))
            text.setDefaultTextColor(QColor("white"))
            text_rect = text.boundingRect()
            text.setPos(x + (24 - text_rect.width()) / 2, y + (24 - text_rect.height()) / 2)

    def draw_piece(self, painter, piece_char, x_pos, y_pos):
        if self.is_red_at_bottom:
            y_pos = 9 - y_pos
        else:
            x_pos = 8 - x_pos

        x = 20 + 26 * x_pos - 26 // 2 + 1
        y = 20 + 26 * y_pos - 26 // 2 + 1

        painter.setBrush(QBrush(QColor("blue")))
        painter.drawEllipse(x, y, 24, 24)
        painter.setFont(QFont("Arial", 12, QFont.Bold))  # Set font for the text
        painter.setPen(QColor("white"))  # Set pen color for text
        painter.drawText(x + 6, y + 18, piece_char)  # Draw the piece character

    def draw_position(self, painter):
        for i, pos in enumerate(self.piece_renderer.piece_positions):
            if pos > 89:
                continue
            x_pos = pos // 10
            y_pos = pos % 10
            self.draw_piece(
                painter, self.piece_renderer.piece_name[i], x_pos, y_pos
            )


class ChessboardView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = Chessboard()
        self.setScene(self.scene)


class ChessTable(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # Chessboard image
        self.chessboard = QLabel(self)
        self.chessboard.setPixmap(QPixmap("Bitmap/XQBoard.bmp"))
        layout.addWidget(self.chessboard)

        # Tabs for additional information
        self.tabs = QTabWidget()
        self.tabs.addTab(QWidget(), "Red Pieces")
        self.tabs.addTab(QWidget(), "Black Pieces")
        layout.addWidget(self.tabs)

        self.setLayout(layout)


class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About XQStudio")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("XQStudio Version 1.63\nDeveloped by Mr. Dong Shiwei"))
        self.setLayout(layout)


class WizardDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wizard Mode")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Wizard functionality is under development."))
        self.setLayout(layout)


class TipsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tips and Tricks")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Here are some tips and tricks for using XQStudio."))
        self.setLayout(layout)


class MoveListHandler:
    def __init__(self):
        self.step_list_xyf = [0] * 512
        self.step_list_xyt = [0] * 512
        self.step_no = 0
        self.step_num = 0

    def initialize_move_list(self, move_list_param):
        if move_list_param:
            steps = move_list_param.split(",")
            for i, step in enumerate(steps):
                from_pos, to_pos = step.split("-")
                self.step_list_xyf[i] = int(from_pos)
                self.step_list_xyt[i] = int(to_pos)
            self.step_num = len(steps)


class BitmapLoader:
    def __init__(self):
        self.bitmaps = {}

    def load_bitmap(self, name, path):
        self.bitmaps[name] = QPixmap(path)

    def get_bitmap(self, name):
        return self.bitmaps.get(name, None)


class EventHandler:
    def __init__(self, chessboard_view):
        self.chessboard_view = chessboard_view

    def handle_event(self, event):
        if event.type() == QEvent.MouseButtonPress:
            pos = event.pos()
            self.process_click(pos)

    def process_click(self, pos):
        # Logic to handle chessboard clicks
        x = pos.x() // 26
        y = pos.y() // 26
        print(f"Clicked position: ({x}, {y})")


class PositionInitializer:
    def __init__(self):
        self.piece_positions = [100] * 32

    def initialize_position(self, position_param):
        if not position_param:
            position_param = "I0,H0,G0,F0,E0,D0,C0,B0,A0,H2,B2,I3,G3,E3,C3,A3|A9,B9,C9,D9,E9,F9,G9,H9,I9,B7,H7,A6,C6,E6,G6,I6"
        positions = position_param.split("|")
        for i, pos in enumerate(positions[0].split(",")):
            self.piece_positions[i] = int(pos[1]) * 10 + ord(pos[0]) - ord("A")


class ChessPieceRenderer:
    def __init__(self):
        self.piece_name = "RHEAKAEHRCCPPPPPrheakaehrccppppp"
        self.piece_init_xy = [100] * 32
        self.piece_curr_xy = [100] * 32
        self.step_list_xyf = [0] * 512
        self.step_list_xyt = [0] * 512
        self.step_no = 0
        self.step_num = 0
        self.is_red_at_bottom = True

    def draw_piece(self, painter, piece_char, x_pos, y_pos):
        if self.is_red_at_bottom:
            y_pos = 9 - y_pos
        else:
            x_pos = 8 - x_pos

        x = 20 + 26 * x_pos - 26 // 2 + 1
        y = 20 + 26 * y_pos - 26 // 2 + 1

        if piece_char == "r":
            self.draw_blk_r(painter, x, y)
        elif piece_char == "h":
            self.draw_blk_h(painter, x, y)
        elif piece_char == "c":
            self.draw_blk_c(painter, x, y)
        elif piece_char == "k":
            self.draw_blk_k(painter, x, y)
        elif piece_char == "a":
            self.draw_blk_a(painter, x, y)
        elif piece_char == "e":
            self.draw_blk_e(painter, x, y)
        elif piece_char == "R":
            self.draw_red_r(painter, x, y)
        elif piece_char == "H":
            self.draw_red_h(painter, x, y)
        elif piece_char == "C":
            self.draw_red_c(painter, x, y)
        elif piece_char == "K":
            self.draw_red_k(painter, x, y)
        elif piece_char == "A":
            self.draw_red_a(painter, x, y)
        elif piece_char == "E":
            self.draw_red_e(painter, x, y)

    def draw_blk_r(self, painter, x, y):
        painter.setBrush(QBrush(QColor("blue")))
        painter.drawEllipse(x, y, 24, 24)
        painter.setBrush(QBrush(QColor("white")))
        # Add specific drawing logic for 'r'

    def draw_red_r(self, painter, x, y):
        painter.setBrush(QBrush(QColor("red")))
        painter.drawEllipse(x, y, 24, 24)
        painter.setBrush(QBrush(QColor("white")))
        # Add specific drawing logic for 'R'

    def draw_blk_h(self, painter, x, y):
        painter.setBrush(QBrush(QColor("blue")))
        painter.drawEllipse(x, y, 24, 24)
        painter.setBrush(QBrush(QColor("white")))
        painter.drawLine(x + 5, y + 5, x + 19, y + 19)
        painter.drawLine(x + 19, y + 5, x + 5, y + 19)

    def draw_red_h(self, painter, x, y):
        painter.setBrush(QBrush(QColor("red")))
        painter.drawEllipse(x, y, 24, 24)
        painter.setBrush(QBrush(QColor("white")))
        painter.drawLine(x + 5, y + 5, x + 19, y + 19)
        painter.drawLine(x + 19, y + 5, x + 5, y + 19)

    def draw_blk_c(self, painter, x, y):
        painter.setBrush(QBrush(QColor("blue")))
        painter.drawEllipse(x, y, 24, 24)
        painter.setBrush(QBrush(QColor("white")))
        painter.drawRect(x + 8, y + 8, 8, 8)

    def draw_red_c(self, painter, x, y):
        painter.setBrush(QBrush(QColor("red")))
        painter.drawEllipse(x, y, 24, 24)
        painter.setBrush(QBrush(QColor("white")))
        painter.drawRect(x + 8, y + 8, 8, 8)

    def draw_blk_k(self, painter, x, y):
        painter.setBrush(QBrush(QColor("blue")))
        painter.drawEllipse(x, y, 24, 24)
        painter.setBrush(QBrush(QColor("white")))
        painter.drawLine(x + 12, y + 4, x + 12, y + 20)

    def draw_red_k(self, painter, x, y):
        painter.setBrush(QBrush(QColor("red")))
        painter.drawEllipse(x, y, 24, 24)
        painter.setBrush(QBrush(QColor("white")))
        painter.drawLine(x + 12, y + 4, x + 12, y + 20)

    def draw_blk_a(self, painter, x, y):
        painter.setBrush(QBrush(QColor("blue")))
        painter.drawEllipse(x, y, 24, 24)
        painter.setBrush(QBrush(QColor("white")))
        painter.drawLine(x + 8, y + 8, x + 16, y + 16)

    def draw_red_a(self, painter, x, y):
        painter.setBrush(QBrush(QColor("red")))
        painter.drawEllipse(x, y, 24, 24)
        painter.setBrush(QBrush(QColor("white")))
        painter.drawLine(x + 8, y + 8, x + 16, y + 16)

    def draw_blk_e(self, painter, x, y):
        painter.setBrush(QBrush(QColor("blue")))
        painter.drawEllipse(x, y, 24, 24)
        painter.setBrush(QBrush(QColor("white")))
        painter.drawLine(x + 6, y + 6, x + 18, y + 18)

    def draw_red_e(self, painter, x, y):
        painter.setBrush(QBrush(QColor("red")))
        painter.drawEllipse(x, y, 24, 24)
        painter.setBrush(QBrush(QColor("white")))
        painter.drawLine(x + 6, y + 6, x + 18, y + 18)


class XQFileHeader:
    def __init__(self):
        self.signature = None
        self.version = None
        self.key_mask = None
        self.product_id = None
        self.key_or_a = None
        self.key_or_b = None
        self.key_or_c = None
        self.key_or_d = None
        self.keys_sum = None
        self.key_xy = None
        self.key_xyf = None
        self.key_xyt = None
        self.qizi_xy = [0] * 32
        self.play_step_no = None
        self.who_play = None
        self.play_result = None
        self.play_nodes = None
        self.ptree_pos = None
        self.reserved1 = [0] * 4
        self.code_a = None
        self.code_b = None
        self.code_c = None
        self.code_d = None
        self.code_e = None
        self.code_f = None
        self.code_h = None
        self.code_g = None
        self.title_a = ""
        self.title_b = ""
        self.match_name = ""
        self.match_time = ""
        self.match_addr = ""
        self.red_player = ""
        self.blk_player = ""
        self.time_rule = ""
        self.red_time = ""
        self.blk_time = ""
        self.reservedh = ""
        self.rmk_writer = ""
        self.author = ""
        self.reserved2 = [0] * 16
        self.reserved3 = [0] * 512


class XQPlayNode:
    def __init__(self):
        self.xyf = None
        self.xyt = None
        self.child_tag = None
        self.reserved = None
        self.remark_size = None


class XQFile:
    def __init__(self, name, play_tree):
        self.name = name
        self.play_tree = play_tree
        self.file_header = None
        self.is_disable_rmk = False
        self.is_reverse_h = False
        self.key_xy = 0
        self.key_xyf = 0
        self.key_xyt = 0
        self.key_rmk_size = 0

    def load_xq_file(self, only_head=False):
        # Logic to load XQF file
        pass

    def save_xq_file(self):
        # Logic to save XQF file
        pass

    def set_random_security_keys(self):
        # Logic to set random security keys
        pass

    def calculate_security_keys(self):
        # Logic to calculate security keys
        pass

    def is_keys_sum_zero(self):
        # Logic to check if keys sum is zero
        pass


class XQFileStream:
    def __init__(self, file_path):
        self.file_path = file_path
        self.key_bytes = [0] * 4
        self.keys_32 = [0] * 32
        self.buffer_1024 = [0] * (1023 + 16)

    def set_key_bytes(self, b1, b2, b3, b4):
        self.key_bytes = [b1, b2, b3, b4]

    def read(self, count):
        # Logic to read from file stream
        pass


class XQStudioApp(QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.setApplicationName("XQStudio 1.63")

        # Initialize main window
        self.main_window = MainWindow()
        self.main_window.show()

        # Initialize other forms
        self.about_window = AboutWindow()
        self.wizard_window = WizardWindow()
        self.tips_dialog = TipsDialog()
        self.search_window = SearchWindow()
        self.table_window = TableWindow()


class AboutWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About XQStudio")
        self.setGeometry(200, 200, 400, 300)
        layout = QVBoxLayout()
        layout.addWidget(QLabel("XQStudio Version 1.63\nDeveloped by Mr. Ng Heng Khai"))
        self.setLayout(layout)

    def exec_(self):
        self.exec()  # Correctly invoke the modal dialog


class SearchWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search XQF Files")
        self.setGeometry(100, 100, 724, 427)
        self.setStyleSheet(BACKGROUND_COLOR)

        # Add components
        self.label = QLabel("Search Window", self)
        self.label.setGeometry(10, 10, 200, 30)

        self.search_button = QPushButton("Search", self)
        self.search_button.setGeometry(10, 50, 100, 30)
        self.search_button.clicked.connect(self.on_search)

    def on_search(self):
        print("Search button clicked")

        # Implement a basic search functionality
        search_term = "example"  # Replace with actual input from a search field
        print(f"Searching for: {search_term}")

        # Example logic: Search through a predefined list of items
        items = ["example1", "example2", "example3"]
        results = [item for item in items if search_term in item]

        if results:
            print("Search results:", results)
        else:
            print("No results found.")


class TableWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table Window")
        self.setGeometry(100, 100, 740, 456)
        self.setStyleSheet(BACKGROUND_COLOR)

        # Add components
        self.label = QLabel("Table Window", self)
        self.label.setGeometry(10, 10, 200, 30)

        self.close_button = QPushButton("Close", self)
        self.close_button.setGeometry(10, 50, 100, 30)
        self.close_button.clicked.connect(self.close)


class WizardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create New XQF File")
        self.setGeometry(100, 100, 521, 359)
        self.setStyleSheet(BACKGROUND_COLOR)

        # Add components
        self.label = QLabel("Wizard Window", self)
        self.label.setGeometry(10, 10, 200, 30)

        self.create_button = QPushButton("Create", self)
        self.create_button.setGeometry(10, 50, 100, 30)
        self.create_button.clicked.connect(self.on_create)

    def on_create(self):
        print("Create button clicked")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("XQStudio 1.63")

        # Initialize handlers
        self.position_initializer = PositionInitializer()

        # Main layout
        layout = QVBoxLayout()

        # Add chessboard view
        self.chessboard_view = QGraphicsView()
        self.chessboard = Chessboard()
        self.chessboard.draw_board()
        self.chessboard.initialize_pieces()
        self.chessboard_view.setScene(self.chessboard)
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

        # Ensure QPushButton and its clicked signal are correctly initialized and connected
        self.search_button = QPushButton("Search", self)
        self.search_button.setGeometry(10, 50, 100, 30)
        self.search_button.clicked.connect(self.on_search)  # Ensure this connection is valid

    def show_about(self):
        dialog = AboutWindow()
        dialog.exec_()

    def show_wizard(self):
        dialog = WizardDialog()
        dialog.exec_()

    def show_tips(self):
        dialog = TipsDialog()
        dialog.exec_()

    def on_search(self):
        print("Search button clicked")
        
        # Implement a basic search functionality
        search_term = "example"  # Replace with actual input from a search field
        print(f"Searching for: {search_term}")

        # Example logic: Search through a predefined list of items
        items = ["example1", "example2", "example3"]
        results = [item for item in items if search_term in item]

        if results:
            print("Search results:", results)
        else:
            print("No results found.")


# Main entry point for the Python version of XQStudio.
if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    logging.info("Starting XQStudio Application...")

    app = XQStudioApp()
    sys.exit(app.exec_())
