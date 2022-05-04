# 封装的类--功能部分
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        QShortcut(QKeySequence(self.tr("Ctrl+W")), self, self.close)
        self.setWindowTitle("")
        self.resize(500, 500)
        self.setup_ui()
        self.rb = QRubberBand(QRubberBand.Rectangle)

    def setup_ui(self):

        # 添加多个复选框子控件
        for i in range (0, 30):
            cb = QCheckBox(self)
            cb.setText("{}".format(i))
            cb.move(i%4*50, i//4*60)
    def mousePressEvent(self, evt):
        # 按下后创建橡皮筋选中控件

        # 尺寸大小，鼠标点击位置
        self.rb.setGeometry(QRect(evt.pos(),QSize()))
        # 展示橡皮筋控件
        self.rb.show()
    def mouseMoveEvent(self, evt):
        # 调整橡皮筋选中控件的位置以及尺寸
        self.rb.resize(QSize)
    def mouseReleaseEvent(self, evt):
        pass

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())