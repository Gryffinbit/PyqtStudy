# 封装的类--功能部分
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        QShortcut(QKeySequence(self.tr("Ctrl+W")), self, self.close)
        self.setWindowTitle("QDateTimeedit")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 设置展示格式
        dte = QDateTimeEdit(self)
        dte.setDisplayFormat("yy-MM-dd")
        return None
        # dte = QDateTimeEdit(self)
        # dt = QDateTime(2022, 2, 3, 14, 23, 33)
        # print(dt)
        dte = QDateTime.currentDateTime()
        QDateTimeEdit(dte, self)

    # 获取从开始计时，到现在所经历的时间
        time = QTime.currentTime()
        time.start()

        btn = QPushButton(self)
        btn.setText("button")
        btn.move(100, 100)
        btn.clicked.connect(lambda : print(time.elapsed()))


#  测试这些类里的功能是否有效，该py下面的类被其他文件调用的时候，不会运行这个main。仅用于功能测试

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())