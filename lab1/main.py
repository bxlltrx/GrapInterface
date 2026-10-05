import sys
from pathlib import Path

from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Первая лабораторная")
        self.resize(600, 500)

        # Надпись
        self.label = QLabel("Нажмите кнопку, чтобы увидеть изображение")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Кнопка
        self.button = QPushButton("Показать изображение")
        self.button.clicked.connect(self.show_image)

        # Размещение элементов в окне
        layout = QVBoxLayout()
        layout.addWidget(self.label, stretch=1)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def show_image(self):
        image_path = Path(__file__).resolve().parent / "image.jpg"
        picture = QPixmap(str(image_path))

        if picture.isNull():
            self.label.setText("Не удалось загрузить image.jpg")
            return

        picture = picture.scaled(
            450, 350,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.label.setPixmap(picture)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())