import sys
from PySide6.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt

from components.framelessWindow import FramelessWindow
from components.main_view import MainContentView
from components.sidebar import Sidebar
from components.statusBar import StatusBar
from utils.theme_loader import load_stylesheet

class ASAPApp(FramelessWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ASAP Download Manager")
        self.resize(1100, 700)
        self.setup_body()

    def setup_body(self):
        # Horizontal layout for Sidebar + Main Content
        central_layout = QHBoxLayout(self.content_area)
        central_layout.setContentsMargins(0, 0, 0, 0)
        central_layout.setSpacing(0)

        self.sidebar = Sidebar(self)
        self.main_content = MainContentView(self)
        
        central_layout.addWidget(self.sidebar)
        central_layout.addWidget(self.main_content, 1)

        # Status Bar at the bottom of the container
        self.status_bar = StatusBar(self)
        self.container_layout.addWidget(self.status_bar)

    def apply_theme_to_all(self, checked):
        """Called by the TitleBar toggle to propagate changes"""
        dynamic_color = "#222222" if checked else "#ffffff"
        
        self.sidebar.update_theme_icons(dynamic_color)
        self.main_content.update_theme_icons(dynamic_color)
        self.status_bar.update_theme_icons(dynamic_color)

def main():
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling)
    app.setAttribute(Qt.AA_UseHighDpiPixmaps)

    try:
        app.setStyleSheet(load_stylesheet("dark_neon"))
    except:
        pass

    window = ASAPApp()
    
    # Connect the TitleBar toggle to our multi-component update method
    window.title_bar.theme_toggle.toggled.connect(window.apply_theme_to_all)
    
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()