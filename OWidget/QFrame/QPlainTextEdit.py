# 封装的类--功能部分
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        QShortcut(QKeySequence(self.tr("Ctrl+W")), self, self.close)
        self.setWindowTitle("")
        self.resize(700, 700)
        self.setup_ui()

    def setup_ui(self):
        pte = QPlainTextEdit(self)
        pte.resize(400, 400)
        pte.move(100, 100)
        # 使得其他函数可以获取它的局部变量
        # 把局部变量，绑定到self身上
        self.pte = pte

        # 添加测试按钮
        btn = QPushButton(self)
        btn.setText("test")
        btn.move(200, 600)
        btn.clicked.connect(self.btn_test)

        # 执行的函数

    def btn_test(self):
        # self.block()
        # self.zoom()
        self.scroll_cursor()
    def scroll_cursor(self):
        # 滚动保证光标可见
        self.pte.centerCursor()
        self.pte.setFocus()
    def zoom(self):
        self.pte.zoomIn(10)    # >0 放大  <0  缩小
    def block(self):
        self.pte.setMaximumBlockCount(3)
    def format_setting(self):
        tcf = QTextCharFormat()
        tcf.setFontUnderline(True)
        tcf.setUnderlineColor(QColor(174, 238, 238))
        self.pte.setCurrentCharFormat(tcf)
    def read_only(self):
        self.pte.setReadOnly(True)
        self.pte.setPlainText("this is test text")
    def tips(self):
        # 占位提示文本
        self.pte.setPlaceholderText("input.....")
#  测试这些类里的功能是否有效，该py下面的类被其他文件调用的时候，不会运行这个main。仅用于功能测试

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())