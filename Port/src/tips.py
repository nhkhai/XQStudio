from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel


class TipsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tips and Tricks")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Here are some tips and tricks for using XQStudio."))
        self.setLayout(layout)
