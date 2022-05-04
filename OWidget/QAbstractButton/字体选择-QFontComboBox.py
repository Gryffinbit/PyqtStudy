# 封装的类--功能部分
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        QShortcut(QKeySequence(self.tr("Ctrl+W")), self, self.close)
        self.setWindowTitle("字体")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 用于字体改变
        label = QLabel(self)
        label.setText("你好 fuck you")
        label.move(100, 100)
        qf = QFontComboBox(self)
        qf.currentFontChanged.connect(lambda font : label.setFont(font))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())