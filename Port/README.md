# XQStudio Python Edition

This project is a Python-based rewrite of the original Delphi and Java XQStudio program.

## Features
- Cross-platform support (Windows and macOS).
- Recreated UI using PyQt or Tkinter.
- Compiled binaries for native execution.

## How to Run
1. Install Python 3.9 or later.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the program:
   ```bash
   python src/main.py
   ```

## How to Compile Binaries
1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Compile for Windows:
   ```bash
   pyinstaller --onefile src/main.py
   ```
3. Compile for macOS:
   ```bash
   pyinstaller --onefile src/main.py
   ```

## Notes
- This is a work in progress. Additional features and modules will be added as the conversion progresses.
