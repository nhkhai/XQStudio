# about.py

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel


class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About XQStudio")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("XQStudio Version 1.63\nDeveloped by Mr. Dong Shiwei"))
        self.setLayout(layout)
