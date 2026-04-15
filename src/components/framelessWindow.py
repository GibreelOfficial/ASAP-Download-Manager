import sys
from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame

class CustomTitleBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(10, 0, 10, 0)
        
        self.app_logo = QLabel("🚀") # Replace with QPixmap for your logo
        self.title_text = QLabel("ASAP Download Manager")
        
        self.btn_min = QPushButton("-")
        self.btn_max = QPushButton("▢")
        self.btn_close = QPushButton("✕")
        
        # Assign object names for your QSS themes
        self.btn_min.setObjectName("minBtn")
        self.btn_max.setObjectName("maxBtn")
        self.btn_close.setObjectName("closeBtn")

        self.setup_platform_ui()
        
        self.btn_min.clicked.connect(self.parent.showMinimized)
        self.btn_max.clicked.connect(self.handle_maximize)
        self.btn_close.clicked.connect(self.parent.close)

    def setup_platform_ui(self):
        # Clear existing layout items if any
        while self.layout.count():
            item = self.layout.takeAt(0)
            if item.widget(): item.widget().hide()

        if sys.platform == "darwin": # macOS Style
            self.layout.addWidget(self.btn_close)
            self.layout.addWidget(self.btn_min)
            self.layout.addWidget(self.btn_max)
            self.layout.addStretch()
            self.layout.addWidget(self.title_text)
            self.layout.addWidget(self.app_logo)
        else: # Windows / Linux Style
            self.layout.addWidget(self.app_logo)
            self.layout.addWidget(self.title_text)
            self.layout.addStretch()
            self.layout.addWidget(self.btn_min)
            self.layout.addWidget(self.btn_max)
            self.layout.addWidget(self.btn_close)

    def handle_maximize(self):
        if self.parent.isMaximized():
            self.parent.showNormal()
        else:
            self.parent.showMaximized()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.initial_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            delta = QPoint(event.globalPosition().toPoint() - self.initial_pos)
            self.parent.move(self.parent.x() + delta.x(), self.parent.y() + delta.y())
            self.initial_pos = event.globalPosition().toPoint()

class FramelessWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Central container for the actual UI (allows for rounded corners via CSS)
        self.container = QFrame()
        self.container.setObjectName("windowContainer")
        self.container_layout = QVBoxLayout(self.container)
        self.container_layout.setContentsMargins(0, 0, 0, 0)
        self.container_layout.setSpacing(0)

        self.title_bar = CustomTitleBar(self)
        self.content_area = QWidget() # This is where your Sidebar and Download Cards go
        
        self.container_layout.addWidget(self.title_bar)
        self.container_layout.addWidget(self.content_area, 1)
        
        self.main_layout.addWidget(self.container)