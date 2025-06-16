from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel


class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search XQF Files")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Search functionality is under development."))
        self.setLayout(layout)
