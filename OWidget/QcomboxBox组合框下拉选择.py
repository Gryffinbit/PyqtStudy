
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        QShortcut(QKeySequence(self.tr("Ctrl+W")), self, self.close)
        self.setWindowTitle("组合框")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        cb = QComboBox(self)
        # cb.addItem("hello")
        # cb.addItem("hello2")
        # cb.insertItem(2, "fuck")
        # cb.insertItem(3 ,"fuck")
        # 同时添加多个选项,传入可迭代对象，str
        cb.addItems(["1", "2", "3"])
        # 设置默认显示的文本（要从选项里选）
        cb.setCurrentText("2")
        # 可被编辑，往里面添加内容
        cb.setEditable(True)

        # 获取数据
        # print(cb.currentText())
 
        # 与用户交互 激活状态
        cb.activated[str].connect(lambda val : print("条目被更新",val))










#  测试这些类里的功能是否有效，该py下面的类被其他文件调用的时候，不会运行这个main。仅用于功能测试

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())