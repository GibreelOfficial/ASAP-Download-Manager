import sys
import os
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt

# Importing your custom components
from components.framelessWindow import FramelessWindow
from utils.theme_loader import load_stylesheet

class ASAPApp(FramelessWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("ASAP Download Manager")
        self.resize(950, 600)
        
        # Adding dummy content to the content_area defined in FramelessWindow
        self.setup_body()

    def setup_body(self):
        # This layout goes inside the content_area of the frameless shell
        layout = QVBoxLayout(self.content_area)
        layout.setContentsMargins(20, 20, 20, 20)
        
        placeholder_label = QLabel("Download Manager Content Goes Here")
        placeholder_label.setAlignment(Qt.AlignCenter)
        placeholder_label.setStyleSheet("font-size: 18px; color: #666;")
        
        layout.addWidget(placeholder_label)

def main():
    app = QApplication(sys.argv)
    
    # 1. Load the dynamic theme from your JSON/QSS logic
    # Make sure you have 'dark_neon.json' in your themes folder
    try:
        theme_style = load_stylesheet("dark_neon")
        app.setStyleSheet(theme_style)
    except FileNotFoundError as e:
        print(f"Warning: Theme files not found. Starting with default style. {e}")

    # 2. Initialize and show the window
    window = ASAPApp()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()