# 封装的类--功能部分
from PyQt5.Qt import *

class SB(QSpinBox):
    # 自定义显示内容
    def textFromValue(self, p_int):
        print(p_int)
        return str(p_int) + "*" + str(p_int)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        QShortcut(QKeySequence(self.tr("Ctrl+W")), self, self.close)
        self.setWindowTitle("QSpinBox")
        self.resize(500, 500)
        self.setup_ui()


    def setup_ui(self):
        sb = SB(self)
        self.sb = sb
        sb.resize(100, 25)
        sb.move(100, 100)


        btn = QPushButton(self)
        btn.setText("test")
        btn.move(100, 300)
        btn.clicked.connect(self.value)

        # 传递信号，用中括号来改变类型
        sb.valueChanged[str].connect(lambda val:print(type(val),val ))

    def value(self):
        # 设置、获取数值
        self.sb.setValue(7)
        print(self.sb.value())
    def base(self):
        # 设置显示的进制
        self.sb.setDisplayIntegerBase(16)

    def prefix_Suffix(self):
        # 设置前缀、后缀
        # 举例，设置星期
        self.sb.setRange(0, 6)
        self.sb.setPrefix("周")
        # 设置特殊字符串，比如说周日
        self.sb.setSpecialValueText("周日")  # 是最开始显示的那一个

    def set_StepSize(self):
        self.sb.setSingleStep(3)
    def Numerical_loop(self):
        # 数值循环
        self.sb.setWrapping(True)
    def max_min(self):
        # 设置步长范围
        self.sb.setMaximum(200)





#  测试这些类里的功能是否有效，该py下面的类被其他文件调用的时候，不会运行这个main。仅用于功能测试

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())