import os
import sys

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

import pytest
from PyQt5.QtWidgets import QApplication
from Port.src.main import SearchWindow  # Ensure correct import of SearchWindow

class TestSearchWindow:
    @pytest.fixture(scope="class")
    def app(self):
        app = QApplication([])
        yield app
        app.quit()

    @pytest.fixture(scope="class")
    def search_window(self, app):
        window = SearchWindow()
        yield window

    def test_search_button_click(self, search_window, capsys):
        # Simulate search button click
        search_window.on_search()

        # Capture printed output
        captured = capsys.readouterr()
        assert "Search button clicked" in captured.out

    def test_search_functionality(self, search_window, capsys):
        # Simulate search functionality
        search_window.on_search()

        # Capture printed output
        captured = capsys.readouterr()
        assert "Searching for: example" in captured.out
        assert "Search results: ['example1', 'example2', 'example3']" in captured.out
