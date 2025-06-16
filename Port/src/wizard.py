from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel


class WizardDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wizard Mode")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Wizard functionality is under development."))
        self.setLayout(layout)
