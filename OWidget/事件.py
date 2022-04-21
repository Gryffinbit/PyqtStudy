# 封装的类--功能部分
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("事件消息")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        pass
        # lable = QLabel(self)
        # lable.setText("hello world")
    def showEvent(self, QShowEvent):
        print("窗口被打开了")
    def closeEvent(self, QCloseEvent):
        print("窗口被关闭")
    def moveEvent(self, QMoveEvent):
        print("窗口被移动")
    def resizeEvent(self, QResizeEvent):
        print("窗口被调整尺寸大小了")
    def enterEvent(self, QEvent):
        print("鼠标进来了")
        self.setStyleSheet("background-color:red;")
    def leaveEvent(self, QEvent):
        print("鼠标离开了")
        self.setStyleSheet("background-color:green;")
    def mousePressEvent(self, QMouseEvent):
        print("鼠标被按下")
        self.setStyleSheet("background-color:blue;")
    def mouseReleaseEvent(self, QMouseEvent):
        print("鼠标被释放")
        self.setStyleSheet("background-color:yellow;")
#  测试这些类里的功能是否有效，该py下面的类被其他文件调用的时候，不会运行这个main。仅用于功能测试
    def keyPressEvent(self, QKeyEvent):
        print("键盘上某个按键被按下")
    def keyReleaseEvent(self, QKeyEvent):
        print("键盘上的按键被释放")
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window =Window()
    window.show()
    sys.exit(app.exec())