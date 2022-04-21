# 封装的类--功能部分
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("test")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        lable = QLabel(self)
        lable.setText("hello world")

#  测试这些类里的功能是否有效，该py下面的类被其他文件调用的时候，不会运行这个main。仅用于功能测试

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window =Window()
    window.show()
    sys.exit(app.exec())