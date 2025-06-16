from PyQt5.QtGui import QPixmap


class BitmapLoader:
    def __init__(self):
        self.bitmaps = {}

    def load_bitmap(self, name, path):
        self.bitmaps[name] = QPixmap(path)

    def get_bitmap(self, name):
        return self.bitmaps.get(name, None)
