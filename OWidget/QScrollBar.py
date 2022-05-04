# 封装的类--功能部分
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        QShortcut(QKeySequence(self.tr("Ctrl+W")), self, self.close)
        self.setWindowTitle("QScrollBar")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        sb = QScrollBar(self)
        sb.resize(20, 500)

        
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())